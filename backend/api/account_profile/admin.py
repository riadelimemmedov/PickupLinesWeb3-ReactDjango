# Django Methods and Function
from django.contrib import admin
from django.apps import apps
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


# Module and Serializers
from .models import AccountProfile


# Register your models here.


#!AccountProfileAdmin
class AccountProfileAdmin(admin.ModelAdmin):
    fields = ["account", "website_links", "city", "state", "country"]


# *Registered Model
admin.site.register(AccountProfile, AccountProfileAdmin)
