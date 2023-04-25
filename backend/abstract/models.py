# Django Methods and Function
from django.db import models
from django.utils import timezone
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

# Custom QuerySet and Manager
from .managers import SoftDeletionManager

# Create your models here.


#!SoftDeletionModel
class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(_("deleted at"), blank=True, null=True)
    restored_at = models.DateTimeField(_("restored at"), blank=True, null=True)
    is_deleted = models.BooleanField(_("is deleted"), default=False)

    objects: SoftDeletionManager = SoftDeletionManager(
        alive_only=True
    )  # Return not deleted objects from database
    all_objects: SoftDeletionManager = SoftDeletionManager(
        alive_only=False
    )  # Return deleted and not deleted objects from databse

    class Meta:
        abstract = True

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def restore(self):
        self.restored_at = timezone.now()
        self.is_deleted = False
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()
