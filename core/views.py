from django.shortcuts import render,redirect
from core.forms import SignupForm, EditProfileForm
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import User

from core.models import Profile
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

def profile_edit(request, id):
    profile=Profile.objects.get(id=id)
    form=EditProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'core/profile_edit.html', {'profile': profile, 'form': form})

def profile(request):
    profile_posts = Post.objects.filter(author=request.user)

    return render(request, 'core/profile.html', {'profile_posts': profile_posts})
