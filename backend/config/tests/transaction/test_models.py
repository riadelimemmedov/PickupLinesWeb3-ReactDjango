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
        # Creates a transaction object with block_hash and gas_fees values
        obj = transaction_factory(
            block_hash="0xf5185e77c12872a94ffa690bca62413cbc50cb95cafb594ba1213b0fbbbfdce2",
            gas_fees="649992",
        )
        # Tests the string representation of the transaction object
        assert obj.__str__() == f"{obj.block_hash} -- {obj.gas_fees}"

    def test_blockhash_transactionhash_max_length(self, transaction_factory):
        # Creates a blockhash and transactionhash string that exceeds the maximum allowed length
        blockhash = "x" * 55
        transactionhash = "y" * 40
        # Creates a transaction object with the blockhash and transactionhash value
        obj = transaction_factory(
            block_hash=blockhash, transaction_hash=transactionhash
        )

        # Gets the maximum length for the block_hash field
        max_length_field_block_hash = Transaction._meta.get_field(
            "block_hash"
        ).max_length

        # Gets the maximum length for the transaction_hash field
        max_length_field_transaction_hash = Transaction._meta.get_field(
            "transaction_hash"
        ).max_length

        # If blockhash or transactionhash value  is too long,raises a validation error when cleaning the object
        if (
            len(blockhash) > max_length_field_block_hash
            or len(transactionhash) > max_length_field_transaction_hash
        ):
            print("If work transaction and block")
            with pytest.raises(ValidationError) as e:
                obj.full_clean()
        # Otherwise,asserts thet the blockhash and transactionhash value is within the allowed length
        else:
            print("Else work transaction and block")
            assert len(blockhash) <= max_length_field_block_hash
            assert len(transactionhash) <= max_length_field_transaction_hash

    def test_fromuser_touser_max_length(self, transaction_factory):
        # Creates a fromuser and touser string that exceeds the maximum allowed length
        fromuser = "x" * 55
        touser = "y" * 65
        # Creates a transaction object with the from_user and to_user value
        obj = transaction_factory(from_user=fromuser, to_user=touser)

        # Gets the maximum length for the from_user and to_user field
        max_length_field_from_user = Transaction._meta.get_field("from_user").max_length
        max_length_field_to_user = Transaction._meta.get_field("to_user").max_length

        # If fromuser or t value  is too long,raises a validation error when cleaning the object
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
        # Creates a transaction object with a specific block_hash number
        obj = transaction_factory(
            block_hash="0xf5185e77c12872a94ffa690bca62413cbc50cb95cafb594ba1213b0fbbbfdce2"
        )
        # Tries to create another transaction object with same block_hash value,expecting an integrity error
        with pytest.raises(IntegrityError) as e:
            print("Work unique handler BLOCK successfully")
            transaction_factory(
                block_hash="0xf5185e77c12872a94ffa690bca62413cbc50cb95cafb594ba1213b0fbbbfdce2"
            )

    def test_transactionhash_unique_field(self, transaction_factory):
        # Creates a transaction object with a specific transaction_hash number
        obj = transaction_factory(
            transaction_hash="0x1c433de9855df9940f7fbde7328646531eceeaab10f30e2127ef05e3df236416"
        )
        # Tries to create another transaction object with same transaction_hash value,expecting an integrity error
        with pytest.raises(IntegrityError) as e:
            print("Work unique handler TRANSACTION successfully")
            transaction_factory(
                transaction_hash="0x1c433de9855df9940f7fbde7328646531eceeaab10f30e2127ef05e3df236416"
            )

    def test_is_complete_false_default(self, transaction_factory):
        # Creates a block object with default values
        obj = transaction_factory()
        # Asserts that the default value for is_complete is False
        print("Work test complete false default")
        assert obj.is_complete is False

    def test_return_transaction_is_complete_only_true(self, transaction_factory):
        # Createas two transaction objects, one with is_complete set True and the other to False
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
        # Queries for transaction that have is_complete set to True
        qs = Transaction.objects.get_is_complete().count()
        assert qs == 1

    # tests that the get_is_complete() method of the Transaction model returns only the Transaction objects where is_complete is False.
    def test_return_transaction_is_complete_only_false(self, transaction_factory):
        # Createas two transaction objects, one with is_complete set True and the other to False
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
        # Queries for transaction that have is_complete set to False
        qs = Transaction.objects.all().count()
        assert qs == 2

    # tests that check default length of block_hash field
    def test_blockhash_transactionhash_default_length(self, transaction_factory):
        # Create transaction object for default length test
        obj = transaction_factory(
            block_hash="0x4b9faeb4b57d8548bd4edc8eaadca715b0f3f03ead21bf5c862a8634107d93ff",
            transaction_hash="0x2d29cb1339d3bf7469aeb8de68745e8fad2250cef19682216453dd53de0e1ed5",
            is_complete=True,
        )
        # The assert statement checks whether the length of the block_hash attribute is equal to 66 and also transaction_hash.
        assert len(obj.block_hash) == 66 and len(obj.transaction_hash) == 66

    def test_fromuser_touser_default_length(self, transaction_factory):
        # Create transaction object for default length test
        obj = transaction_factory(
            block_hash="0x4b9faeb4b57d8548bd4edc8eaadca715b0f3f03ead21bf5c862a8634107d93ff",
            transaction_hash="0x2d29cb1339d3bf7469aeb8de68745e8fad2250cef19682216453dd53de0e1ed5",
            from_user="0x3c44cdddb6a900fa2b585dd299e03d12fa4293bc",
            to_user="0x9fe46736679d2d9a65f0992f2272de9f3c7fa6e0",
            is_complete=True,
        )
        # The assert statement checks whether the length of the from_user and to_user objec length is equal to 42 or not.
        assert len(obj.from_user) == 42 and len(obj.to_user) == 42


#!TestBlockModel
class TestBlockModel:
    def test_str_method(self, block_factory):
        # Creates a block object with block number and time stamp values
        obj = block_factory(
            block_number="51", time_stamp="2023-05-01T09:42:47.037411+04:00"
        )
        # Tests the string representation of the block object
        assert obj.__str__() == f"{obj.block_number} -- {obj.time_stamp}"

    def test_blockminer_max_length(self, block_factory):
        # Creates a block miner string that exceeds the maximum allowed length
        blockminer = "x" * 120
        # Creates a block object with the block miner value
        obj = block_factory(block_miner=blockminer)
        # Gets the maximum length for the block miner field
        max_length_field_block_miner = Block._meta.get_field("block_miner").max_length
        # If the block miner value is too long, raises a validation error when cleaning the object
        if len(blockminer) > max_length_field_block_miner:
            print("If work blockminer")
            with pytest.raises(ValidationError) as e:
                obj.full_clean()
        # Otherwise, asserts that the block miner value is within the allowed length
        else:
            print("Else work blockminer")
            assert len(blockminer) <= max_length_field_block_miner

    def test_block_number_unique_field(self, block_factory):
        # Creates a block object with a specific block number
        obj = block_factory(block_number=52)
        # Tries to create another block object with the same block number, expecting an integrity error
        with pytest.raises(IntegrityError) as e:
            block_factory(block_number=52)

    def test_is_complete_false_default(self, block_factory):
        # Creates a block object with default values
        obj = block_factory()
        # Asserts that the default value for is_complete is False
        assert obj.is_complete is False

    def test_return_block_is_complete_only_true(self, block_factory):
        # Creates two block objects, one with is_complete set to True and the other to False
        block_factory(block_number=51, is_complete=True)
        block_factory(block_number=52, is_complete=False)
        # Queries for blocks that have is_complete set to True
        qs = Block.objects.get_is_complete().count()
        # Asserts that only one block was returned
        assert qs == 1

    def test_return_block_is_complete_only_false(self, block_factory):
        # Creates two block objects, one with is_complete set to True and the other to False
        block_factory(block_number=51, is_complete=True)
        block_factory(block_number=52, is_complete=False)
        # Queries for all blocks

    def test_block_miner_default_length(self, block_factory):
        # Create block object
        obj = block_factory(
            id=22,
            block_number=2,
            block_miner="0xe0a2bd4258d2768837baa26a28fe71dc079f84c7",
            is_complete=True,
            time_stamp="2023-05-02T07:00:16.688228+04:00",
        )
        # The assert statemen   t checks whether the length of the block_miner attribute is equal to 42.
        assert len(obj.block_miner) == 42
