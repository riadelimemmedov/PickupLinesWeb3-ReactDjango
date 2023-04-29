# Django Methods and Function
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


# Module and Serializers
from .models import Account

# Register your models here.


#!AccountAdmin
@admin.register(Account)
class AccountAdmin(UserAdmin):
    # thumbnail
    def thumbnail(self, object):
        if object.account_picture:
            return format_html(
                '<img src="{}" width="50" style="border-radius:50%;">'.format(
                    object.account_picture.url
                )
            )
        else:
            return format_html(
                '<img src="https://i.stack.imgur.com/l60Hf.png" width="35" style="border-radius:50%;">'
            )

    thumbnail.allow_tags = True
    thumbnail.short_description = "Account Picture"

    fieldsets = (
        (None, {"fields": ("email", "phone", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "account_picture",
                    "registration_number",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "role",
                )
            },
        ),
    )
    add_fieldsets = (  # When you add new user to database list this column for added to database
        (
            None,
            {
                "classes": ("wide"),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "account_picture",
                    "phone",
                    "password1",
                    "password2",
                    "role",
                ),
            },
        ),
    )
    list_display = [
        "first_name",
        "last_name",
        "phone",
        "is_staff",
        "date_joined",
        "last_login",
        "role",
        "thumbnail",
    ]
    list_filter = [
        "is_staff",
        "is_superuser",
        "is_admin",
        "is_superadmin",
        "is_active",
    ]
    list_display_links = ["first_name", "last_name", "thumbnail"]
    search_fields = ["first_name", "last_name", "email", "phone"]
    readonly_fields = ["date_joined", "last_login"]
