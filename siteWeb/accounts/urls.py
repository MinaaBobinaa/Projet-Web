from django.urls import path
from accounts import views
from .views import loginView, logoutView, profileRegisterView
from . import views

urlpatterns = [
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
    path('profileRegister', views.profileRegisterView),
    # path('register/', profileRegisterView, name='register'),
    path('submit_registration/', views.profileRegisterView, name='submit_registration'),
    path('registration_success/', views.registration_success, name='registration_success'),

]
