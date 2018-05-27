from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .models import Sub, Thread, Comment
from django.shortcuts import render, get_object_or_404

from django.views import generic
from django.views.generic import View

from .forms import UserForm


def index(request):

    subs = Sub.objects.all()

    # renders the template file: subs/templates/subs/index.html
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


def view_sub(request, sub_name):

    sub = Sub.objects.get(name=sub_name)
    threads = Thread.objects.filter(sub__in=Sub.objects.filter(id=sub.id))

    if threads:
        return HttpResponse("Welcome to " + sub.name)#render(request, 'music/sub_detail.html', {'threads': threads})
    else:
        return HttpResponse("No threads yet!")