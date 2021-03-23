"""Users views"""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Exception
from django.db.utils import IntegrityError
# Create your views here.


@login_required
def update_profile(request):
    """ Update a user's profile view """
    return render(request, 'users/update_profile.html')


def login_view(request):
    """ login view """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')   
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and/or password'})

    return render(request, 'users/login.html')


def signup(request):
    """ sign up for new users """
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in use'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')
    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    """ Logout an user """
    logout(request)
    return redirect('login')
