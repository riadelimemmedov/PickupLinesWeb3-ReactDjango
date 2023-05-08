# Pytest
import pytest
import factory


# Python Modules
import json

# * If you don't declare pytestmark our test class model don't accsess to database table
pytestmark = pytest.mark.django_db


#!TestTransactionEndPoint
class TestTransactionEndPoint:
    # A class-level variable that holds the endpoint of the transaction API.
    endpoint = "/api/transactions/"

    # A test method that tests retrieving all transactions from the API.
    def test_transaction_get_all(self, transaction_factory, api_client):
        # Creating four fake transaction objects with unique block_hash and transaction_hash fields using the transaction_factory fixture.
        transaction_factory.create_batch(
            4,
            block_hash=factory.Sequence(lambda n: "Transaction_Block_Hash_%d" % n),
            transaction_hash=factory.Sequence(lambda n: "Transaction_Hash_%d" % n),
            is_complete=True,
        )

        # Sending a GET request to the transaction endpoint using the api_client fixture and storing the response object in response variable.
        response = api_client().get(self.endpoint, format="json")

        # Check retrieved response status code equal to 200 or not.
        assert (
            response.status_code == 200
        ), "Encounter error when send to request get all transaction"

        # Asserting that the length of the retrieved transaction list is 4, indicating that all created transactions have been retrieved successfully.
        assert (
            len(json.loads(response.content)) == 4
        ), "Created Transaction object length must be equal to 4"

    # A test method that tests retrieving a single transaction from the API.
    def test_transaction_get_single(self, transaction_factory, api_client):
        # Creating a single fake transaction object using the transaction_factory fixture and storing it in obj.
        obj = transaction_factory(
            block_hash=factory.Sequence(lambda n: "Transaction_Block_Hash_%d" % n),
            transaction_hash=factory.Sequence(lambda n: "Transaction_Hash_%d" % n),
            is_complete=True,
        )
        # Sending a GET request to the transaction endpoint with the created transaction's primary key appended to the endpoint URL and storing the response object in response.
        response = api_client().get(f"{self.endpoint}{obj.pk}/", format="json")
        # Parsing the response content and storing the retrieved transaction object in a list for assertion.
        transaction_list = []
        transaction_list.append(json.loads(response.content.decode("utf-8")))

        # Asserting that the response status code is 200, indicating a successful request.
        assert (
            response.status_code == 200
        ), "No transaction was found matching the transaction primary key"

        # Asserting that the length of the retrieved transaction list is 1, indicating that the created transaction has been retrieved successfully.
        assert len(transaction_list) == 1, "Transaction List not equal to 1"

    # A test method that tests creating a new transaction via the API.
    # def test_transaction_create(self, transaction_factory, api_client):

    #     response = api_client().post(
    #         "http://127.0.0.1:8000/api/transaction/create",
    #         {
    #             "pickup_object": {
    #                 "blockHash": "",  # This field unique at the database
    #                 "from": "",  # Sended user account
    #                 "to": "",  # Received user account
    #                 "transactionHash": "",  # This field unique at the database
    #                 "transactionIndex": "0",
    #                 "status": 1,
    #                 "gasUsed": "701235",
    #                 "blockNumber": "12",
    #             }
    #         },
    #     )
    #     assert response.status_code == 200


#!TestBlockEndpoint
class TestBlockEndpoint:
    # A class-level variable that holds the endpoint of the block API.
    endpoint = "/api/blocks/"

    # A test method that tests retrieving all blocks from the API.
    def test_block_get_all(self, block_factory, api_client):
        # Creating four fake block objects with unique block_number and block_miner fields using the block_factory fixture.
        block_factory.create_batch(
            4,
            block_number=factory.Sequence(lambda n: "Block_Number_%d" % n),
            block_miner=factory.Sequence(lambda n: "Block_Miner_%d" % n),
            is_complete=True,
        )

        # Sending a GET request to the block endpoint using the api_client fixture and storing the response object in response variable
        response = api_client().get(self.endpoint, format="json")

        # Check retrieved response status code equal to 200 or not.
        assert (
            response.status_code == 200
        ), "Encounter error when send to request get all blocks"

        # Asserting that the length of the retrieved transaction list is 4,indicating that all created transactions have been retrieved successfully
        assert (
            len(json.loads(response.content)) == 4
        ), "Created Block objects length must be equal to 4"

    def test_block_get_single(self, block_factory, api_client):
        # Creating a single fake block object using block_factory fixture and store in obj variable
        obj = block_factory(
            block_number=factory.Sequence(lambda n: "Block_Number_%d" % n),
            block_miner=factory.Sequence(lambda n: "Block_Miner_%d" % n),
            is_complete=True,
        )

        # Sending a GET request to the block endpoint with created block's primary key appended to the endpoint URL and storing the response object in response
        response = api_client().get(f"{self.endpoint}{obj.pk}/", format="json")

        # Parsing the response content and storing the retrieved block object in a list for assertion
        block_list = []
        block_list.append(json.loads(response.content.decode("utf-8")))

        # Asserting that the response status code is 200,indicating a succsessful request
        assert (
            response.status_code == 200
        ), "No block was found matching the block primary key"

        # Asserting that the length of the retrieved block list is 1,indicating that the created block has beed retrieved successfully
        assert len(block_list) == 1, "Block List not equal to 1"
