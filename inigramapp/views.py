from django.shortcuts import render
from .models import Post, User
from .forms import PostForm

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post=form.save()
            post.author=request.user
            post.save()
            return redirect('/')
    else:
        form=PostForm()
    return render(request, 'inigramapp/new_post.html',{'form': form})            
