# Factories
import factory

from api.transaction.models import Transaction, Block


#!TransactionFactory
class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    block_hash = "0xf5185e77c12872a94ffa690bca62413cbc50cb95cafb594ba1213b0fbbbfdce2"
    from_user = "0x3c44cdddb6a900fa2b585dd299e03d12fa4293bc"
    to_user = "0x9fe46736679d2d9a65f0992f2272de9f3c7fa6e0"
    transaction_hash = (
        "0x1c433de9855df9940f7fbde7328646531eceeaab10f30e2127ef05e3df236416"
    )
    transaction_index = "5"
    is_complete = False
    gas_fees = "649992"
