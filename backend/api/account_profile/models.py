# Python Modules and Functions
import sys

# Create custom path for impor other models file from another path,if you not define this django not found app and
sys.path.append("..")


# Django Methods and Function
from django.db import models
from django.db.models.signals import post_save
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

# Module and Serializers
from account.models import Account

# Helpers Function and Database Modules
from config.helpers import get_profile_photo_upload_path


# Create your models here.

#!Profile
class AccountProfile(models.Model):
    account = models.OneToOneField(
        Account, verbose_name=_("account"), on_delete=models.CASCADE
    )
    website_links = models.URLField(_("website links"), default="")
    city = models.CharField(_("city"), max_length=20)
    state = models.CharField(_("state"), max_length=20)
    country = models.CharField(_("country"), max_length=20)

    class Meta:
        verbose_name = "Account Profile"
        verbose_name_plural = "Account Profiles"

    def __str__(self) -> str:
        return str(self.account.first_name)

    @property
    def get_full_address(self) -> str:
        return f"{self.city} -- {self.country}"


# *create_account_profile => signals
def create_account_profile(sender, instance, created, **kwargs):
    if created:
        AccountProfile.objects.create(account=instance)


post_save.connect(create_account_profile, Account)
