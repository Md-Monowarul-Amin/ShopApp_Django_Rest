import statistics
from django.shortcuts import render
from rest_framework.views import APIView

from .managers import CustomUserManager

from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class RegisterUserView(APIView):

    def post(self, request, *args, **kwargs):

        data = {
            'email' : request.data.get('email'),
            'first_name' : request.data.get('first_name'),
            'last_name' : request.data.get('last_name'),
            'password' : request.data.get('password'),
        }
        print(data)
        serializer = UserSerializer(data=data)
        user = CustomUser.objects.create_user(data['email'], data['password'], data['first_name'], data['last_name'])
        user.save()
        #serializer.create_user(self, data, request.password)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
