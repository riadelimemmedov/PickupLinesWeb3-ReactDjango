# Django
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

# Serializers and Models
from account.models import Account


# Django Rest
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.response import Response


# Third Party
from djoser.serializers import TokenCreateSerializer


#!CustomTokenSerializer
class CustomTokenSerializer(TokenCreateSerializer):
    # validate
    def validate(self, data):
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")
        metamask_address = data.get("metamask_address")

        if not email:
            raise serializers.ValidationError("Email is required")

        if not username:
            raise serializers.ValidationError("Username is required")

        if not password:
            raise serializers.ValidationError("Password is required")

        if not metamask_address:
            raise serializers.ValidationError("Metamask Address is required")

        return data
