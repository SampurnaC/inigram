from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your title',
        'class': 'form-control'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Enter Your description',
        'class': 'form-control'
    }))

    class Meta:
        model= Post
        fields=['title', 'description']

class CommentForm(forms.ModelForm):

    
    # body = forms.CharField(
    #     label= '',
    #     widget=forms.Textarea(attrs={
    #     'placeholder': 'Add a Comment',
    #     'class': 'form-control mt-5'
    # }))

    class Meta:
        model= Comment
        fields=['body']
