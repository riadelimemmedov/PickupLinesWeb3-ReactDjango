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


#!api_client
@pytest.fixture  # Fixtures are functions,which will run before each test function to which it is applied.Fixtures are used to feed some data to the tests such as database connections,URLs to test and some sort of input data.
def api_client():
    return APIClient
