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

# Create your views here.


#!TransactionViewSet
class TransactionListRetrieveViewSet(viewsets.ViewSet):

    """
    A Viewset for viewing all Transaction
    """

    queryset = Transaction.objects.get_is_complete()
    serializer_class = TransactionSerializer
    lookup_field = "pk"

    @permission_classes([IsAdminUser, AdminRequired])
    def list(self, request):
        serializer = TransactionSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes([IsAdminUser, AdminRequired])
    def retrieve(self, request, pk=None):
        transaction = get_object_or_404(self.queryset, pk=pk)
        serializer = TransactionSerializer(transaction, many=False)
        return Response(serializer.data)


#!TransactionCreateViewSet
class TransactionCreateViewSet(viewsets.ViewSet):

    """
    A Viewset for create Transaction
    """

    queryset = Transaction.objects.get_is_complete()

    def create_block(self, request):
        url = "http://127.0.0.1:8000{}/{}".format(
            request.path.replace("transaction", "block"),
            request.data["pickup_object"]["blockNumber"],
        )
        requests.post(url)

    @permission_classes([IsAdminUser, IsAuthenticated, AdminRequired, ProfileRequired])
    def create(self, request):
        pickup_object = request.data["pickup_object"]

        if pickup_object["status"]:
            transaction_obj = Transaction.objects.create(
                block_hash=pickup_object["blockHash"],
                from_user=pickup_object["from"],
                to_user=pickup_object["to"],
                transaction_hash=pickup_object["transactionHash"],
                transaction_index=pickup_object["transactionIndex"],
                is_complete=True if pickup_object["status"] == True else False,
                gas_fees=pickup_object["gasUsed"],
            )
            transaction_obj.save()
            self.create_block(request)

            return HttpResponse(
                "Is created transaction successfully", status=status.HTTP_201_CREATED
            )

        else:
            return HttpResponse(
                "Error occured when creating transaction",
                status=status.HTTP_400_BAD_REQUEST,
            )


#!BlockListRetrieveViewSet
class BlockListRetrieveViewSet(viewsets.ViewSet):

    """
    A Viewset for viewing all Block
    """

    queryset = Block.objects.get_is_complete()
    serializer_class = BlockSerializer
    lookup_field = "pk"

    @permission_classes([IsAdminUser, AdminRequired])
    def list(self, request):
        serializer = BlockSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes([IsAdminUser, AdminRequired])
    def retrieve(self, request, pk=None):
        transaction = get_object_or_404(self.queryset, pk=pk)
        serializer = BlockSerializer(transaction, many=False)
        return Response(serializer.data)


#!BlockCreateViewSet
class BlockCreateViewSet(viewsets.ViewSet):
    """
    A Viewset for create Block
    """

    queryset = Block.objects.get_is_complete()

    @permission_classes([IsAdminUser, IsAuthenticated, AdminRequired, ProfileRequired])
    def create(self, request, block_number=None):
        url = "https://api-goerli.etherscan.io/api?module=block&action=getblockreward&blockno={}&apikey={}".format(
            block_number, config("API_KEY_GEORLI")
        )
        response = requests.get(url, timeout=1).json()

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
            return HttpResponse(
                "Error occured when creating block", status=status.HTTP_400_BAD_REQUEST
            )
