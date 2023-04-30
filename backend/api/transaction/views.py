# Django
from django.shortcuts import render, get_object_or_404


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
    serializer_class = TransactionSerializer

    @permission_classes([IsAdminUser, IsAuthenticated, AdminRequired, ProfileRequired])
    def create(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction_obj = Transaction.objects.create(**serializer.validated_data)
            return Response(
                TransactionSerializer(transaction_obj).data,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    serializer_class = BlockSerializer

    def create(self, request):
        serializer = BlockSerializer(data=request.data)
        if serializer.is_valid():
            block_obj = Block.objects.create(**serializer.validated_data)
            return Response(
                BlockSerializer(block_obj).data, status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
