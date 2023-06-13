from django.shortcuts import render,redirect
from core.forms import SignupForm
from django.http import HttpResponse


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
    return render(request, 'core/index.html')
