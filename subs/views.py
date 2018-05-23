from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Sub, Post, Comment

from django.views import generic
from django.views.generic import View

from .forms import UserForm


def index(request):

    subs = Sub.objects.all()

    return render(request, 'subs/index.html', {'subs': subs})


def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                # subs = subs.objects.get_all...
                return render(request, 'subs/')


# process data
def register(request):
    form = UserForm(request.POST or None)

    if form.is_valid():

        user = form.save(commit=False)

        # format data
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # hash the password
        user.set_password(password)

        # save user to database
        user.save()

        # attempt to log the user in and return the User object
        user.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                # log the user in
                login(request, user)

                return redirect('subs:index')
