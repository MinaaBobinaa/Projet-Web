from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ProfileRegisterForm, ProfileModelForm
from .models import ProfileModel
import main
import main.views
from django.urls import reverse
# Create your views here.

def loginView(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,  user)
            # if request.GET.get('next'):
            return HttpResponseRedirect(reverse(main.views.house_list))
        else:
            context={
                "username":username,
                "errorMessage": "Error: The username you entered does not exist. Please try again."
            }
            return render(request,"accounts/login.html", context)
        
    else:
        return render(request,"accounts/login.html",{})
    
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(main.views.index))


def profileRegisterView(request):
    if request.method == "POST":
        user_form = ProfileRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            profile = ProfileModel(user=user)
            profile.save()
            return render(request, "accounts/registration_success.html") 
    else:
        user_form = ProfileRegisterForm()
    return render(request, "accounts/profileRegister.html", {
        'user_form': user_form
    })

def registration_success(request):
    return render(request, "accounts/registration_success.html")