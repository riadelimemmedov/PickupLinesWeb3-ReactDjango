from django.shortcuts import render
from djoser.views import TokenCreateView
from .serializers import CustomTokenSerializer

from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# Create your views here.


#!CustomTokenCreateSerializer
class CustomTokenCreateSerializer(TokenCreateView):
    serializer_class = CustomTokenSerializer
