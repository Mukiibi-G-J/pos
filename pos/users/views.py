from calendar import c
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from  . import forms




def signup(request):
    # this will help us redirect the user to the login page 
    # if request.user.is_anonymous():
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            form.save()
            new_user = authenticate(username=username, email=email, password=password)
            if new_user is not None:
                    redirect("signin")
        else: 
            print('invaild input')       
    else:
        form = forms.SignupForm()
    
    # else:
    #     redirect("login")
    context ={
        'form':form
    }
    return render(request, 'user/signup.html', context)
    
    
def signin(request):
    return render(request, 'user/login.html' )