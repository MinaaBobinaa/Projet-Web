from django.urls import path
from .views import house_list
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("house/", house_list, name='house_list'),
]