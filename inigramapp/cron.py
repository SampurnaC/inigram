from .models import Post
from django.contrib.auth.models import User
import random

def print_hello():
    user=User.objects.last()
    number=random.randint(0,100)
    Post.objects.create(title=number, description=number, author=user)
