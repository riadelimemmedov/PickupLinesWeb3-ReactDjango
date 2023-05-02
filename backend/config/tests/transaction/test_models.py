# Django modules and function
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db import transaction

# Models and Serializers
from api.transaction.models import Transaction, Block


# Pytest
import pytest


# * If you don't declare pytestmark our test class model don't accsess to database table
pytestmark = pytest.mark.django_db


#!TestTransactionModel
class TestTransactionModel:
    def test_str_method(self, transaction_factory):
        obj = transaction_factory(
            block_hash="0xf5185e77c12872a94ffa690bca62413cbc50cb95cafb594ba1213b0fbbbfdce2",
            gas_fees="649992",
        )
        assert obj.__str__() == f"{obj.block_hash} -- {obj.gas_fees}"

    def test_blockhash_transactionhash_max_length(self, transaction_factory):
        blockhash = "x" * 55
        transactionhash = "y" * 40
        obj = transaction_factory(
            block_hash=blockhash, transaction_hash=transactionhash
        )

        max_length_field_block_hash = Transaction._meta.get_field(
            "block_hash"
        ).max_length
        max_length_field_transaction_hash = Transaction._meta.get_field(
            "transaction_hash"
        ).max_length

        if (
            len(blockhash) > max_length_field_block_hash
            or len(transactionhash) > max_length_field_transaction_hash
        ):
            print("If work transaction and block")
            with pytest.raises(ValidationError) as e:
                obj.full_clean()
        else:
            print("Else work transaction and block")
            assert len(blockhash) <= max_length_field_block_hash
            assert len(transactionhash) <= max_length_field_transaction_hash

    def test_fromuser_touser_max_length(self, transaction_factory):
        fromuser = "x" * 55
        touser = "y" * 65
        obj = transaction_factory(from_user=fromuser, to_user=touser)

        max_length_field_from_user = Transaction._meta.get_field("from_user").max_length
        max_length_field_to_user = Transaction._meta.get_field("to_user").max_length

        if (
            len(fromuser) > max_length_field_from_user
            or len(touser) > max_length_field_from_user
        ):
            print("IF work fromuser and touser")
            with pytest.raises(ValidationError) as e:
                obj.full_clean()
        else:
            print("Else work fromuser and touser")
            assert len(fromuser) <= max_length_field_from_user
            assert len(touser) <= max_length_field_to_user

    def test_blockhash_unique_field(self, transaction_factory):
        obj = transaction_factory(
            block_hash="0xf5185e77c12872a94ffa690bca62413cbc50cb95cafb594ba1213b0fbbbfdce2"
        )
        with pytest.raises(IntegrityError) as e:
            print("Work unique handler BLOCK successfully")
            transaction_factory(
                block_hash="0xf5185e77c12872a94ffa690bca62413cbc50cb95cafb594ba1213b0fbbbfdce2"
            )

    def test_transactionhash_unique_field(self, transaction_factory):
        obj = transaction_factory(
            transaction_hash="0x1c433de9855df9940f7fbde7328646531eceeaab10f30e2127ef05e3df236416"
        )
        with pytest.raises(IntegrityError) as e:
            print("Work unique handler TRANSACTION successfully")
            transaction_factory(
                block_hash="0x1c433de9855df9940f7fbde7328646531eceeaab10f30e2127ef05e3df236416"
            )

    def test_is_complete_false_default(self, transaction_factory):
        obj = transaction_factory()
        print("Work test complete false default")
        assert obj.is_complete is False

    def test_return_transaction_is_complete_only_true(self, transaction_factory):
        transaction_factory(
            is_complete=True,
            block_hash="0xf5185e77c12872a94ffa690bca62413cbc50cb95cafb594ba1213b0fbbbfdce2",
            transaction_hash="0x1c433de9855df9940f7fbde7328646531eceeaab10f30e2127ef05e3df236416",
        )
        transaction_factory(
            is_complete=False,
            block_hash="0x4b9faeb4b57d8548bd4edc8eaadca715b0f3f03ead21bf5c862a8634107d93ff",
            transaction_hash="0x4b9faeb4b57d8548bd4edc8eaadca715b0f3f03ead21bf5c862a8634107d93ff",
        )
        qs = Transaction.objects.get_is_complete().count()
        assert qs == 1

    def test_return_transaction_is_complete_only_false(self, transaction_factory):
        transaction_factory(
            is_complete=True,
            block_hash="0xf5185e77c12872a94ffa690bca62413cbc50cb95cafb594ba1213b0fbbbfdce2",
            transaction_hash="0x1c433de9855df9940f7fbde7328646531eceeaab10f30e2127ef05e3df236416",
        )
        transaction_factory(
            is_complete=False,
            block_hash="0x4b9faeb4b57d8548bd4edc8eaadca715b0f3f03ead21bf5c862a8634107d93ff",
            transaction_hash="0x4b9faeb4b57d8548bd4edc8eaadca715b0f3f03ead21bf5c862a8634107d93ff",
        )
        qs = Transaction.objects.all().count()
        assert qs == 2

    def test_blockhash_transactionhash_default_length(self, transaction_factory):
        obj = transaction_factory(
            block_hash="0x4b9faeb4b57d8548bd4edc8eaadca715b0f3f03ead21bf5c862a8634107d93ff",
            transaction_hash="0x2d29cb1339d3bf7469aeb8de68745e8fad2250cef19682216453dd53de0e1ed5",
            is_complete=True,
        )

        assert len(obj.block_hash) == 66 and len(obj.transaction_hash) == 66

    def test_fromuser_touser_default_length(self, transaction_factory):
        obj = transaction_factory(
            block_hash="0x4b9faeb4b57d8548bd4edc8eaadca715b0f3f03ead21bf5c862a8634107d93ff",
            transaction_hash="0x2d29cb1339d3bf7469aeb8de68745e8fad2250cef19682216453dd53de0e1ed5",
            from_user="0x3c44cdddb6a900fa2b585dd299e03d12fa4293bc",
            to_user="0x9fe46736679d2d9a65f0992f2272de9f3c7fa6e0",
            is_complete=True,
        )

        assert len(obj.from_user) == 42 and len(obj.to_user) == 42
