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


# Create your views here.


#!TransactionViewSet
class TransactionListRetrieveViewSet(viewsets.ViewSet):

    """
    A Viewset for viewing all Transaction
    """

    queryset = Transaction.objects.get_is_complete()
    lookup_field = "pk"

    # @permission_classes([IsAdminUser, AdminRequired])
    def list(self, request):
        serializer = TransactionSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes([IsAdminUser, AdminRequired])
    def retrieve(self, request, pk=None):
        transaction = get_object_or_404(self.queryset, pk=pk)
        serializer = TransactionSerializer(transaction, many=False)
        return Response(serializer.data)
