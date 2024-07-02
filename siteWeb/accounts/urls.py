from django.urls import path
from accounts import views
from . import views

urlpatterns = [
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
]
