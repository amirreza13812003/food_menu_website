from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm

def register(request):
    if User.objects.filter(id=request.user.id).exists():
        username = User.objects.filter(id=request.user.id).get()
        messages.success(request, f'You have registered before {username}!')
        return redirect('food:item_list')  
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username} your account is successfully created!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form}) 
    

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f'Welcome {username}, you have been logged in successfully!')
            return redirect('food:item_list')
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, f'You have been logged out successfully')
        return redirect('food:item_list') 

    return render(request, 'users/logout.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')