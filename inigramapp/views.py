from django.shortcuts import render, redirect, get_object_or_404
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

def edit(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "inigramapp/edit.html", {'post': post, 'form': form})

def delete(request, id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('/')
