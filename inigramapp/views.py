from django.shortcuts import render, redirect
from .models import Post, User
from .forms import PostForm

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author=request.user
            post=form.save()
            # post.author=request.user
            post.save()
            return redirect('/')
    else:
        form=PostForm()
    return render(request, 'inigramapp/new_post.html',{'form': form})            

def show(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'inigramapp/show.html', {'post':post})
