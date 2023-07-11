from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, User, Comment
from .forms import PostForm, CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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
    if request.method == "POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            # form.instance.author=request.user
            # form.instance.post=post
            # new_comment=form.save()
            # new_comment.save()

            new_comment=form.save(commit=False)
            new_comment.author=request.user
            new_comment.post=post
            new_comment.save()
            return redirect('/')
    else:
        form=CommentForm()        

    comments = Comment.objects.filter(post=post)

    return render(request, 'inigramapp/show.html', {'form': form, 'post':post, 'comments': comments})

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

@login_required
def like(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":

        
        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like == False:
            post.likes.add(request.user)
        if is_like:
            post.likes.remove(request.user)    

    next = request.POST.get('next', '/')

    return HttpResponseRedirect(next)

@login_required
def dislike(request, id):
    post = Post.objects.get(id=id)
    if request.method=="POST":
       
        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

    next = request.POST.get('next', '/')

    return HttpResponseRedirect(next)
