from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages


def index(request):
    """Returns the render index.html file"""
    return render(request, 'index.html')


def logout(request):
    """ Log out user """
    auth.logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect(reverse('index'))


def login(request):
    """ Return login page """
    return render(request, 'login.html')


def register(request):
    """ Return register page """
    return render(request, 'register.html')


def profile(request):
    """ Return profile page """
    return render(request, 'profile.html')