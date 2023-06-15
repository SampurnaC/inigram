from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import PostForm

urlpatterns = [
    path('new/', views.new, name='create-post'),
    path('show/<int:id>/', views.show, name='show-post'),
    
]
