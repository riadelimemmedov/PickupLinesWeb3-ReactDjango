# RestFramework Function And Module
from rest_framework.test import APIClient


# Pytest
import pytest
from pytest_factoryboy import register


# Factories
from .factories import TransactionFactory, BlockFactory


# *Register TestModelFactory
# if you want call this Factory in the test file you need to declare  bottom_line format = category_factory
register(TransactionFactory)
register(BlockFactory)
