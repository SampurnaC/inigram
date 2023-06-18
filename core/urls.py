from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import SigninForm

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=SigninForm), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/edit/<int:id>/', views.profile_edit, name='edit-profile'),
    path('profile/', views.profile, name='profile'),


]
