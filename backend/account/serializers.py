from djoser.serializers import TokenCreateSerializer
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


#!CustomTokenSerializer
class CustomTokenSerializer(TokenCreateSerializer):
    metamask_address = serializers.CharField()
    username = serializers.CharField()

    def validate(self, attrs):
        metamask_address = attrs.get("metamask_address")
        username = attrs.get("username")

        if metamask_address and username:
            user = authenticate(metamask_address=metamask_address, username=username)
            if not user:
                msg = _("Unable to log in with provided credentials")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _("Must include 'metamask_address'. ")
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs
