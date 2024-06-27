from django.shortcuts import render
from .models import House
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request,'index.html') #La page home du projet

def house_list(request):
    houses = House.objects.all()
    return render(request, 'house_list.html', {'houses': houses})