# Django
from django.shortcuts import render, get_object_or_404, HttpResponse


# Django Rest
from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, permissions

# Models and Serializers
from .models import Transaction, Block
from .serializers import TransactionSerializer, BlockSerializer


# Permission Class
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from account.permissions import AdminRequired, ProfileRequired

# Third Party Packages
import requests
from decouple import config
from drf_spectacular.utils import extend_schema

# Create your views here.


#!TransactionViewSet
# Define a ViewSet for retrieving Transaction objects
class TransactionListRetrieveViewSet(viewsets.ViewSet):

    """
    A Viewset for viewing all Transaction
    """

    # Define the queryset for the ViewSet to retrieve all completed Transaction objects
    queryset = Transaction.objects.get_is_complete()

    # Define the serializer to use for the Transaction objects
    serializer_class = TransactionSerializer

    # Define the lookup field for the Transaction objects
    lookup_field = "pk"

    # Define the list method to retrieve a list of all Transaction objects
    # The method requires admin authentication and permissions
    @permission_classes([IsAdminUser, AdminRequired])
    @extend_schema(responses=TransactionSerializer)
    def list(self, request):
        # Serialize the queryset and return the serialized data
        serializer = TransactionSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Define the retrieve method to retrieve a single Transaction object by its primary key
    # The method requires admin authentication and permissions
    @permission_classes([IsAdminUser, AdminRequired])
    @extend_schema(responses=TransactionSerializer)
    def retrieve(self, request, pk=None):
        # Retrieve the Transaction object with the specified primary key
        transaction = get_object_or_404(self.queryset, pk=pk)
        # Serialize the Transaction object and return the serialized data
        serializer = TransactionSerializer(transaction, many=False)
        return Response(serializer.data)


#!TransactionCreateViewSet
# Define a ViewSet for creating Transaction objects
class TransactionCreateViewSet(viewsets.ViewSet):

    """
    A Viewset for create Transaction
    """

    # Define the queryset for the ViewSet to retrieve all completed Transaction objects
    queryset = Transaction.objects.get_is_complete()

    # Define a method to create a block for the Transaction object
    def create_block(self, request):
        # Construct the URL for the block creation endpoint
        url = "http://127.0.0.1:8000{}/{}".format(
            request.path.replace("transaction", "block"),
            request.data["pickup_object"]["blockNumber"],
        )
        # Send a POST request to the block creation endpoint
        requests.post(url)

    # Define the create method to create a Transaction object
    # The method requires admin and user authentication and permissions
    @permission_classes([IsAdminUser, IsAuthenticated, AdminRequired, ProfileRequired])
    def create(self, request):
        # Extract the pickup_object data from the request data
        pickup_object = request.data["pickup_object"]

        # Check if the pickup_object status is True
        if pickup_object["status"]:
            # Create a new Transaction object with the pickup_object data
            transaction_obj = Transaction.objects.create(
                block_hash=pickup_object["blockHash"],
                from_user=pickup_object["from"],
                to_user=pickup_object["to"],
                transaction_hash=pickup_object["transactionHash"],
                transaction_index=pickup_object["transactionIndex"],
                is_complete=True if pickup_object["status"] == True else False,
                gas_fees=pickup_object["gasUsed"],
            )
            # Save the Transaction object to the database
            transaction_obj.save()
            # Call the create_block method to create a block for the Transaction object
            self.create_block(request)

            # Return a success response if the Transaction object is created successfully
            return HttpResponse(
                "Is created transaction successfully", status=status.HTTP_201_CREATED
            )

        else:
            # Return an error response if the Transaction object creation fails
            return HttpResponse(
                "Error occured when creating transaction",
                status=status.HTTP_400_BAD_REQUEST,
            )


#!BlockListRetrieveViewSet
# Define a ViewSet for retrieving Block objects
class BlockListRetrieveViewSet(viewsets.ViewSet):

    """
    A Viewset for viewing all Block
    """

    # Define the queryset for the ViewSet to retrieve all completed Block objects
    queryset = Block.objects.get_is_complete()
    # Set the serializer class to use for the Block objects
    serializer_class = BlockSerializer
    # Set the lookup field to use for retrieving a single Block object
    lookup_field = "pk"

    # Define the list method to retrieve a list of Block objects
    # The method requires admin authentication and permissions
    @permission_classes([IsAdminUser, AdminRequired])
    def list(self, request):
        # Serialize the queryset of Block objects using the BlockSerializer
        serializer = BlockSerializer(self.queryset, many=True)
        # Return the serialized data as a response with an HTTP 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Define the retrieve method to retrieve a single Block object
    # The method requires admin authentication and permissions
    @permission_classes([IsAdminUser, AdminRequired])
    def retrieve(self, request, pk=None):
        # Get the Block object with the specified primary key, or return a 404 response if not found
        block = get_object_or_404(self.queryset, pk=pk)
        # Serialize the Block object using the BlockSerializer
        serializer = BlockSerializer(block, many=False)
        # Return the serialized data as a response
        return Response(serializer.data)


#!BlockCreateViewSet
class BlockCreateViewSet(viewsets.ViewSet):
    """
    A Viewset for create Block
    """

    # This is a class-level attribute that sets the queryset to retrieve all the completed blocks.
    queryset = Block.objects.get_is_complete()

    # This is a method-level decorator that specifies the required permissions to create a block. The function signature takes in self, request, and an optional block_number
    @permission_classes([IsAdminUser, IsAuthenticated, AdminRequired, ProfileRequired])
    def create(self, request, block_number=None):
        url = "https://api-goerli.etherscan.io/api?module=block&action=getblockreward&blockno={}&apikey={}".format(
            block_number, config("API_KEY_GEORLI")
        )
        # This creates a URL to fetch information about the given block_number from the Goerli network.
        response = requests.get(url, timeout=1).json()

        # This sends an HTTP GET request to the above URL and stores the response in response after parsing it into JSON format.
        # This checks if the response status is "1", indicating success. If it is, a new Block object is created with the given block_number and the miner's address obtained from the response. The is_complete field is set to True if the response status is "1", indicating that the block was successfully created. The object is then saved to the database and an HTTP response is returned with a message and a status code of 201 CREATED.
        if response["status"] == "1":
            obj = Block.objects.create(
                block_number=block_number,
                block_miner=response["result"]["blockMiner"],
                is_complete=True if response["status"] == "1" else False,
            )
            obj.save()
            return HttpResponse(
                "Is created block successfully", status=status.HTTP_201_CREATED
            )
        else:
            # If the response status is not "1", indicating an error, an HTTP response is returned with an error message and a status code of 400 BAD REQUEST.
            return HttpResponse(
                "Error occured when creating block", status=status.HTTP_400_BAD_REQUEST
            )
