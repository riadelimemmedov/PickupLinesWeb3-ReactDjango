# Python Modules and Functions
import sys

# Create custom path for impor other models file from another path,if you not define this django not found app and
sys.path.append("..")


# Django Methods and Function
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import RandomCharField

# Third Party Packages
from django_extensions.db.models import ActivatorModel, TimeStampedModel

# Models and Serializers
from backend.account.models import Profile

# Create your models here.


#!Pickup
class Pickup(TimeStampedModel, ActivatorModel):
    profile = models.ForeignKey(
        Profile,
        verbose_name=_("pickup profile"),
        related_name="pickup_profile",
        on_delete=models.CASCADE,
    )
    address = models.CharField(_("pickup address"), max_length=100)
    block_number = models.PositiveIntegerField(_("block number"))
    gas_used = models.PositiveIntegerField(_("gas used"), default=0)
    status = models.BooleanField(_("status pickup"), default=False)

    class Meta:
        verbose_name = "Pickup"
        verbose_name_plural = "Pickups"

    def __str__(self):
        return f"{self.author.account.first_name} --- {self.address}"


#!LineText
class LineText(TimeStampedModel, ActivatorModel):
    author = models.ForeignKey(
        Profile,
        verbose_name=_("line text author"),
        related_name="linetext_profile",
        on_delete=models.CASCADE,
    )
    pickup = models.ForeignKey(
        Pickup,
        verbose_name=_("pickup for linetext"),
        related_name="linetext_pickup",
        on_delete=models.CASCADE,
    )
    line_description = models.TextField(_("line description"))
    status = models.BooleanField(_("status linetext"), default=False)

    class Meta:
        verbose_name = "LineText"
        verbose_name_plural = "LineTexts"

    def __str__(self):
        return f"{self.author.account.username} --- {self.pickup.address}"


#!FavoritePickup
class FavoritePickup(models.Model):
    profile = models.ForeignKey(
        Profile,
        verbose_name=_("profile"),
        related_name="favorite_pickup_profile",
        on_delete=models.CASCADE,
    )
    pickups = models.ManyToManyField(
        Pickup,
        verbose_name=_("pickups"),
        related_name="favorite_pickups",
        on_delete=models.CASCADE,
    )
    code = RandomCharField(_("code"), length=12, unique=True)

    class Meta:
        verbose_name = "Favorite PickUp"
        verbose_name_plural = "Favorite PickUpLines"

    def __str__(self):
        return f"{self.profile.account.username} --- {self.code}"


# *Like Choices
LIKE_CHOICES = (
    ("Like", "Like"),
    ("Unlike", "Unlike"),
)


#!Like
class Like(TimeStampedModel, ActivatorModel):
    profile = models.ForeignKey(
        Profile,
        verbose_name=_("liked profile"),
        related_name="profile_like",
        on_delete=models.CASCADE,
    )
    pickup = models.ForeignKey(
        Pickup,
        verbose_name=_("liked pickup"),
        related_name="pickup_like",
        on_delete=models.CASCADE,
    )
    value = models.CharField(
        _("like value"), max_length=100, choices=LIKE_CHOICES, default="Like"
    )
    is_profile_liked = models.BooleanField(_("is profile liked"), default=False)

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self):
        return (
            f"{self.profile.account.username} --- {self.pickup.address} -- {self.value}"
        )
