# Django and Django Rest
from rest_framework import serializers

# Models
from .models import Transaction, Block


#!TransactionSerializer
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


#!BlockSerializer
class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = "__all__"
