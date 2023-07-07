from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment, User
# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import message
from .forms import CommentForm

@login_required
def comment_list(request):
    comments = message.objects.all().order_by('-created_at')
    return render(request, 'comments/comment_list.html', {'comments': comments})

@login_required
def comment_add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm()
    
    return render(request, 'comments/comment_add.html', {'form': form})



def home(request):
    return render(request, 'contact/home.html')

def contact(request):
    if request.method == 'POST':
        context = Comment()
        name =request.POST.get('name')
        email =request.POST.get('email')
        subject =request.POST.get('subject')
        body =request.POST.get('body')
        context.subject = subject
        context.name = name
        context.email = email
        context.body = body
        context.save()
        return HttpResponse('<h1> THANK YOU FOR CONTACTING US.  </h1>')
    return render(request, 'contact/contact.html')

def contact_thankyou(request):
    form = Comment.objects.all()
    context ={
        'form':form,
    }
    return render(request, 'contact/contact_thankyou.html', context)




def user_list(request):
    users = User.objects.all()
    return render(request, 'contact/user_list.html', {'users': users})
