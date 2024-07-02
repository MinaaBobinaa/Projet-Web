from django.urls import path
from .views import house_list
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("house/", views.house_list, name='house_list'),
    path('timeview/', views.timeView, name='timeView'),
]