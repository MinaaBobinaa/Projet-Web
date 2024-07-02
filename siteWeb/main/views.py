from django.shortcuts import render
from .models import House
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import accounts
# Create your views here.


def index(request):
    return render(request,'index.html') #La page home du projet

def house_list(request):
    houses = House.objects.all()
    return render(request, 'house_list.html', {'houses': houses})

# @login_required
def timeView(request):
    # if request.user.is_authenticated and request.user.is_active:
        houses = House.objects.all()

        context = {
            "houselist": houses,
        }
        return render(request, "houses/house_list.html", context)
    # else:
    #     return HttpResponseRedirect(reverse(accounts.views.loginView))