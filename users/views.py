from rest_framework.response import Response
from django.shortcuts import render

from users.models import IMUser
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny

from users.serializers import *
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView

from users.utils import *

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def signUp(request):
    username = request.data.get("username")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    phone_number = request.data.get("phone_number")
    password = request.data.get("password")
    
    new_user = IMUser.objects.create(
        username = username,
        first_name = first_name,
        last_name = last_name,
        phone_number = phone_number
    )
    new_user.set_password(password)
    new_user.save()
    # new_user.generate_auth_token()
    serializer = AuthSerializer(new_user, many=False)
    return Response({"message":"Account successfully created", "result": serializer.data})


@api_view(['POST'])
@permission_classes([AllowAny])
def logIn(request):
    #1. receive data from client and validate input
    username = request.data.get("username")
    password = request.data.get("password")
    
    if not username or not password:
        return Response({"detail":"my friend behave yourself and send the right username and password"}, status.HTTP_400_BAD_REQUEST)
    #2. check user existence
    
    try:
        user = IMUser.objects.get(username=username)
        
        auth_user = authenticate(username=username, password=password)

        if auth_user:
            if user.is_active:
                if user.is_blocked:
                    return Response({"detail":"Please you are blocked, contact customer support"}, status.HTTP_400_BAD_REQUEST)
                else:
                    login(request, user)
                    serializer = AuthSerializer(user, many=False)
                    return Response({"result":serializer.data}, status.HTTP_200_OK)
            else:
                return Response({"detail":"please you are inactive"})
        else:
            user.temporal_login_fail += 1
            user.save()
            
            return Response({"detail":"Invalid credentials"}, status.HTTP_400_BAD_REQUEST)
        
    except IMUser.DoesNotExist:
        user.temporal_login_fail += 1
        return Response({"message":"Username does not exist"}, status.HTTP_400_BAD_REQUEST)
    
    
    #3. check user authentication
    #login user
    #respond to users request
    
    
class ForgotPasswordAPIView(APIView):
    permission_classes=[AllowAny]
    
    def post(self, request):
        #1. receive username
        username = request.data.get("username")
        if not username:
            return generate_400_response("Please provide a valid username")
        #2. check if user exist
        try:
            user = IMUser.objects.get(username=username)
            #3. send OTP code
            otp_code = generate_unique_code()
            user.unique_code = otp_code
            user.save()
            # send user an email or SMS at this point
            
            return Response({"detail":"please check your email for an OTP code"}, status.HTTP_200_OK)
        except IMUser.DoesNotExist:
            
            return generate_400_response("Username does not exist")
        
        #4. respond to user
        
class ResetPasswordAPIView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        username = request.data.get("username")
        unique_code = request.data.get("unique_code")
        password = request.data.get("password")
        
        if not (username and unique_code and password):
            return generate_400_response("Please provide the correct username")
        
        try:
            user = IMUser.objects.get(username = username) 
            if not user.unique_code == unique_code:
                return generate_400_response("try again")
            else:
                user.set_password(password)
                user.unique_code = ""
                user.save()
                return Response({"message":"password reset successfully"}, status.HTTP_200_OK)
        except IMUser.DoesNotExist:
            return generate_400_response("username does not exist")

class CurrentUserProfileAPIView(APIView):
    def get(self, request):
        print(request.user)
        return Response(UserSerializer(request.user).data)
    
class ChangePasswordAPIView(APIView):
    def post(self, request):
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        user_obj = request.user
        user = UserSerializer(user_obj).data
        print(user)
        
        if not (old_password and new_password):
            return generate_400_response("field cannot be blank")
        auth_user = authenticate(username=user['username'], password=old_password)
        if auth_user:
            auth_user.set_password(new_password)
            auth_user.save()
            return Response({"message":"password changed successfully"}, status.HTTP_200_OK)
        return generate_400_response('authentication failed')
        
    
