# Django Methods and Function
from django.db.models import Manager

# Custom QuerySet and Manager
from .querysets import SoftDeletionQuerySet


#!SoftDeletionManager
class SoftDeletionManager(Manager):
    def __init__(self, alive_only=True, *args, **kwargs):
        self.alive_only = alive_only
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:  # True return not soft deleted objects
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model).filter(
            deleted_at=not None
        )  # False return all objects

    def hard_delete(self):
        return self.get_queryset().hard_delete()
