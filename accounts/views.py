from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm


def index(request):
    """Returns the render index.html file"""
    return render(request, 'index.html')


@login_required
def logout(request):
    """ Log out user """
    auth.logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect(reverse('index'))


def login(request):
    """ Return login page """
    if request.user.is_authenticated:
        return redirect(reverse("index"))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

        if user:
            auth.login(user=user, request=request)
            messages.success(request, "You have successfully logged in!")
            return redirect(reverse("index"))
        else:
            login_form.add_error(None, "You failed to enter the correct user or password.")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


def register(request):
    """ Return register page """
    return render(request, 'register.html')


@login_required
def profile(request):
    """ Return profile page """
    return render(request, 'profile.html')
