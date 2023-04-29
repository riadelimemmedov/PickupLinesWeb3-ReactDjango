# Django Rest
from rest_framework import permissions


# Models and Serializers
from .models import Account


#!AdminRequired
class AdminRequired(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Account.ADMIN_ROLE_CODE


#!ProfileRequired
class ProfileRequired(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Account.PROFILE_ROLE_CODE
