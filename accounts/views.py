from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('/')