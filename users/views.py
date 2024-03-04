from rest_framework.response import Response
from django.shortcuts import render

from users.models import IMUser
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny

from users.serializers import *
from rest_framework import status
from django.contrib.auth import authenticate, login

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
        if user.is_active:
            user.temporal_login_fail += 1
            return Response({"message":"User is not active"})
        if auth_user:
            login(request, user)
            serializer = AuthSerializer(user, many=False)
            return Response({"result":serializer.data}, status.HTTP_200_OK)
        else:
            return Response({"detail":"Invalid credentials"}, status.HTTP_400_BAD_REQUEST)
        
    except IMUser.DoesNotExist:
        user.temporal_login_fail += 1
        return Response({"message":"Username does not exist"}, status.HTTP_400_BAD_REQUEST)
    
    
    #3. check user authentication
    #login user
    #respond to users request
    
