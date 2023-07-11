from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    title=models.CharField(max_length=50)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.TextField()
    created_on=models.DateTimeField(default=timezone.now)
    likes=models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes=models.ManyToManyField(User, blank=True, related_name='dislikes')
    
    def __str__(self):  
        return self.title

class Comment(models.Model):
    body=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post.title
