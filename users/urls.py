from django.urls import path
from .views import *

urlpatterns = [
    path('users/signup/', signUp),
    path('users/login/', logIn),
    path('users/forgot_password/', ForgotPasswordAPIView.as_view()),
    path('users/reset_password/', ResetPasswordAPIView.as_view()),
    path('users/profile/', CurrentUserProfileAPIView.as_view()),
    path('users/change_password/', ChangePasswordAPIView.as_view())
]
