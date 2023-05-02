from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment, User
# Create your views here.

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
