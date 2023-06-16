from django.shortcuts import render,redirect
from core.forms import SignupForm
from django.http import HttpResponse
from django.contrib.auth import logout
from inigramapp.models import Post

def signup(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form=SignupForm()    
    return render(request, 'core/signup.html', {'form': form})

def index(request):
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'core/index.html', {'posts': posts})

def logout_user(request):
    logout(request)
    return redirect('/')

