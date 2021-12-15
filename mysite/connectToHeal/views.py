from django.shortcuts import  render, redirect
from .forms import createTherapistForm, createUserForm
from .models import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def homepage(request):
    return render(request, "connectToHeal/home.html")

def aboutpage(request):
    return render(request, "connectToHeal/about.html")

def viewBlogs(request):
    blogs = Blog.objects.all()
    return render(request, "connectToHeal/viewBlogs.html", {'blogs': blogs})

def registerUserPage(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save() #creating user - handles already existing user, password validation and everything by default
    
    context = {'form' : form}
    return render(request, "connectToHeal/registerUser.html", context)

def registerTherapistPage(request):
    form = createTherapistForm()
    if request.method == 'POST':
        form = createTherapistForm(request.POST)
        if form.is_valid():
            form.save() #creating user - handles already existing user, password validation and everything by default
    
    context = {'form' : form}
    return render(request, "connectToHeal/registerTherapist.html", context)

def loginPage(request):
    context = {}
    return render(request, "connectToHeal/login.html", context)