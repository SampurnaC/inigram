from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import PostForm



urlpatterns = [
    path('new/', views.new, name='create-post'),
    path('show/<int:id>/', views.show, name='show-post'),
    path('edit/<int:id>/', views.edit, name='edit-post'),
    path('delete/<int:id>/', views.delete, name='delete-post'),
    path('post/<int:id>/like', views.like, name='like-post'),
    path('post/<int:id>/dislike', views.dislike, name='dislike-post'),

    
]


