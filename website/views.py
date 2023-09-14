from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate users
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You've been logged in!")
            return redirect('home')
        else:
            messages.error(request, "There was an error logged in, please try again!")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


# logout user
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out....")
    return redirect('home')


def register(request):
    return render(request, 'register.html', {})