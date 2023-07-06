from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Candidate,ControlVote,Position






def about(request):
    return render(request, "poll/about.html")

def registrationView(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password'] == cd['confirm_password']:
                obj = form.save(commit=False)
                obj.set_password(obj.password)
                obj.save()
                messages.success(request, 'You have been registered.')
                return redirect('home')
            else:
                return render(request, "poll/registration.html", {'form':form,'note':'password must match'})
    else:
        form = RegistrationForm()

    return render(request, "poll/registration.html", {'form':form})

def loginView(request):
    if request.method == "POST":
        usern = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request, username=usern, password=passw)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.success(request, 'Invalid username or password!')
            return render(request, "poll/login.html")
    else:
        return render(request, "poll/login.html")


@login_required
def logoutView(request):
    logout(request)
    return redirect('home')

@login_required
def dashboardView(request):
    return render(request, "dashboard.html")

@login_required
def news(request):
    return render(request, "poll/news.html")

@login_required
def positionView(request):
    positions = Position.objects.all()
    candidates = Candidate.objects.all()
    return render(request, "poll/position.html", {'positions':positions, 'candidates': candidates})


@login_required
def vote(request):
    if request.method == "POST":   

        temp = ControlVote.objects.get_or_create(user=request.user)[0]


        if not temp.status:
            president = request.POST.get("President")
            vice_president = request.POST.get("Vice president")
            fin_sec = request.POST.get("Fin sec")
            gen_sec = request.POST.get("Gen sec")
            social_director = request.POST.get("Social director")
            sports_director = request.POST.get("Sports director")
            ass_gen_sec = request.POST.get("Assistant general secretary")
            pro = request.POST.get("PRO")
            software_director = request.POST.get("Software director")

            president_cand = Candidate.objects.get(id=president)
            president_cand.total_vote += 1
            president_cand.save()

            vice_president_cand = Candidate.objects.get(id=vice_president)
            vice_president_cand.total_vote += 1
            vice_president_cand.save()

            fin_sec_cand = Candidate.objects.get(id=fin_sec)
            fin_sec_cand.total_vote += 1
            fin_sec_cand.save()

            gen_sec_cand = Candidate.objects.get(id=gen_sec)
            gen_sec_cand.total_vote += 1
            gen_sec_cand.save()

            social_director_cand = Candidate.objects.get(id=social_director)
            social_director_cand.total_vote += 1
            social_director_cand.save()

            sports_director_cand = Candidate.objects.get(id=sports_director)
            sports_director_cand.total_vote += 1
            sports_director_cand.save()

            ass_gen_sec_cand = Candidate.objects.get(id=ass_gen_sec)
            ass_gen_sec_cand.total_vote += 1
            ass_gen_sec_cand.save()

            pro_cand = Candidate.objects.get(id=pro)
            pro_cand.total_vote += 1
            pro_cand.save()

            software_director_cand = Candidate.objects.get(id=software_director)
            software_director_cand.total_vote += 1
            software_director_cand.save()

            temp.status = True
            temp.save()

            return HttpResponseRedirect('/position/')
        else:
            messages.success(request, 'you have already voted.')
            return HttpResponseRedirect('/position/')
        

@login_required
def candidateView(request, pos):
    obj = get_object_or_404(Position, pk = pos)
    if request.method == "POST":   

        temp = ControlVote.objects.get_or_create(user=request.user, position=obj)[0]

        if temp.status == False:
            temp2 = Candidate.objects.get(pk=request.POST.get(obj.title))
            temp2.total_vote += 1
            temp2.save()
            temp.status = True
            temp.save()
            return HttpResponseRedirect('/position/')
        else:
            messages.success(request, 'you have already been voted this position.')
            return render(request, 'poll/candidate.html', {'obj':obj})
    else:
        return render(request, 'poll/candidate.html', {'obj':obj})

@login_required
def resultView(request):
    obj = Candidate.objects.all().order_by('position','-total_vote')
    return render(request, "poll/result.html", {'obj':obj})


@login_required
def resultView1(request):
    obj = Candidate.objects.all().order_by('position','-total_vote')
    return render(request, "list.html", {'obj':obj})


@login_required
def candidateDetailView(request, id):
    obj = get_object_or_404(Candidate, pk=id)
    return render(request, "poll/candidate_detail.html", {'obj':obj})


@login_required
def changePasswordView(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, "poll/password.html", {'form':form})

#######################################################################
from django.shortcuts import render, redirect
from .forms import  UserUpdateForm, ProfileUpdateForm

@login_required
# Create your views here.
def profile(request):
    context = {

    }
    return render(request, 'poll/profile.html', context)

@login_required
def editProfileView(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'poll/edit_profile.html', context)

