from django.urls import path
from . import views
from .views import register
urlpatterns =[
    #accounts/register/
    path('register/',views.register, name='register'),
    path('profile/',views.profile, name='profile')    #accounts/profile
]