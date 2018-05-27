from django.contrib.auth.models import User
from django import forms

from .models import Sub, Thread, Comment


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class SubForm(forms.ModelForm):

    class Meta:
        model = Sub
        fields = ['name', 'title', 'description', 'submission_text']


class PostForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ['title', 'url', 'text']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
