from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'class': 'form-control'
    }))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Your Password',
        'class': 'form-control'
    }))
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput(attrs={
        
        'placeholder': 'Your Password Confirmation',
        'class': 'form-control'
    }))
    
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')

class SigninForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control'
    }))
class EditProfileForm(forms.ModelForm):

    bio = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Update Your bio',
        'class': 'form-control'
    }))

    class Meta:
        model= Profile
        fields=['bio']
