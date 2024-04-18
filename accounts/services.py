from accounts.serializers import SignUpSerializer
from utils.custom_responses import success, error, ok, unauthorized
from .serializers import SignUpSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.views import LoginView
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.token import create_jwt_pair_tokens

def create_user_service(request):
    try:
        data = request.data

        serializer = SignUpSerializer(data=data)

        if serializer.is_valid():
                serializer.save()
        
        return success(message="User created succesfully")
    
    except Exception as exc:
         raise Exception("Error creating user" + exc)
    

def login_user_service(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')
        print(email, password)

        user = authenticate(request, email = email, password = password)

        print(user)

        if user is not None:
            if user.is_verified == True:
                print('authenicated')
                tokens = create_jwt_pair_tokens(user)



                data = {
                    "message" : "Login Successful",
                    "token" : tokens,
                    "is_login" : True,
                    "user" : {
                        "user_id" : user.id,
                        "email" : user.email,
                    }
                }
                return ok(response_data=data, message="Login succesful")
            
            else:
                return unauthorized(message="user is not verified")

        else:
            return unauthorized(message="Invalid email or password !")
    except Exception as exc:
        return error("Error in login " + exc)


    