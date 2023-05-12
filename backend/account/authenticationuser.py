# Django
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

# Django Rest
from rest_framework import serializers

# Serializers and Models
from account.models import Account


#!CustomAuthBackend
class CustomAuthBackend(BaseBackend):
    # login_field_validate
    def login_field_validate(self, username, password, metamask_address, email):
        if not username:
            raise serializers.ValidationError("Username is required")

        if not password:
            raise serializers.ValidationError("Password is required")

        if not metamask_address:
            raise serializers.ValidationError("Metamask Address is required")

        if not email:
            raise serializers.ValidationError("Email is required")
        return True

    # authenticate
    def authenticate(
        self, request, username=None, password=None, metamask_address=None, email=None
    ):
        UserModel = Account
        validated_field = self.login_field_validate(
            username, password, metamask_address, email
        )
        if username and metamask_address and email and password and validated_field:
            account = None
            try:
                user = UserModel.objects.filter(
                    username__iexact=username,
                    metamask_address__iexact=metamask_address,
                    email__iexact=email,
                )
                if user.exists() and user.first().check_password(password):
                    return user.first()
                else:
                    raise serializers.ValidationError("Please input credentials valid")
            except UserModel.DoesNotExist:
                return serializers.ValidationError(
                    "User not found match to credentials"
                )

    # get_user
    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
