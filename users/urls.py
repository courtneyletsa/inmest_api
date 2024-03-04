from django.urls import path
from .views import *

urlpatterns = [
    path('users/signup/', signUp),
    path('users/login/', logIn)
]
