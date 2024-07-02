from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
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




    
            