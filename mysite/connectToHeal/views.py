from django.shortcuts import  render, redirect
from .forms import createUserForm, DiscussionForm
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def homepage(request):
    return render(request, "connectToHeal/home.html")
def userhomepage(request):
    return render(request, "connectToHeal/userhome.html")
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
            messages.success(request, "Account has been created for " + form.cleaned_data.get('username') +" successfully!")
            
            
            return redirect('login')
    
    context = {'form' : form}
    return render(request, "connectToHeal/registerUser.html", context)
'''
def registerTherapistPage(request):
    form = createTherapistForm()
    if request.method == 'POST':
        form = createTherapistForm(request.POST)
        if form.is_valid():
            form.save() #creating user - handles already existing user, password validation and everything by default
    
    context = {'form' : form}
    return render(request, "connectToHeal/registerTherapist.html", context)
'''
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # user = authenticate(request, username = username, password = password)
        # if user is not None:
        #     login(request, username)
        #     redirect('userhomepage')
    context = {}
    return render(request, "connectToHeal/login.html", context)


def discussionPage(request):
    form =  DiscussionForm()
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            form.save()
    
    forums= DiscussionModel.objects.all()
        
    return render(request, 'connectToHeal/discussion.html', {'form': form,'forums':forums})        
