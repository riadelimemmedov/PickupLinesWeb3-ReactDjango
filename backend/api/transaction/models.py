# Python Modules and Functions
import sys

# Create custom path for impor other models file from another path,if you not define this django not found app and
sys.path.append("..")


# Django Methods and Function
from django.db import models
from django.utils.translation import gettext_lazy as _

# Custom QuerySet and Manager
from backend.abstract.models import SoftDeletionModel

# Create your models here.


# *ActiveQueryset
class ActiveQueryset(models.QuerySet):
    def get_is_complete(self):
        return self.filter(is_complete=True)


############################################################################################################################################################

#!Transaction
class Transaction(SoftDeletionModel):
    block_hash = models.CharField(_("block hash"), max_length=100, unique=True)
    from_user = models.CharField(_("from user"), max_length=100)
    to_user = models.CharField(_("to user"), max_length=100)
    transaction_hash = models.CharField(
        _("transaction hash"), unique=True, max_length=100
    )
    transaction_index = models.CharField(_("transaction index"), max_length=100)
    is_complete = models.BooleanField(_("is complete transaction"), default=False)
    gas_fees = models.CharField(_("gas fees"), max_length=100)

    # objects
    objects = ActiveQueryset.as_manager()

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return f"{self.block_hash} -- {self.gas_fees}"


#!Block
class Block(models.Model):
    block_number = models.CharField(_("block number"), max_length=100)
    block_miner = models.CharField(_("block miner"), max_length=100)
    is_complete = models.BooleanField(_("is complete"), default=False)
    time_stamp = models.DateTimeField(_("time stamp"), auto_now_add=True)

    # objects
    objects = ActiveQueryset.as_manager()

    class Meta:
        verbose_name = "Block"
        verbose_name_plural = "Blocks"

    def __str__(self):
        return f"{self.block_number} -- {self.time_stamp}"
