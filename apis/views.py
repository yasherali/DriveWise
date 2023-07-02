from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, CustomUserToken
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from .authentication import CustomUserBackend

# Create your views here.

class Signup(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new CustomUser instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                # Generate or retrieve the driver's token
                token, created = CustomUserToken.objects.get_or_create(user=user)
                return Response({"message": "Login Successful", 'token': token.key})
        except CustomUser.DoesNotExist:
            pass

        return Response({"message": "Invalid login credentials"}, status=status.HTTP_401_UNAUTHORIZED)
