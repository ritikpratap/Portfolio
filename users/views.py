from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, RegisterForm

# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('index')

    return render(request,'users/login.html',{'form':form})

def register_view(request):
    if request.method=="POST":
        form = RegisterForm(request.POST or None)

        if form.is_valid():

            user = form.save()
            login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request,"Created Successfully!!!")
            return redirect('index')

    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.success(request,"You logged Out!")
    return redirect('login')