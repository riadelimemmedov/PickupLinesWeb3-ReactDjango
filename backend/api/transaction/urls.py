# Django
from django.urls import path, include

# Django Rest
from rest_framework.routers import DefaultRouter

# Views,Model,Serializers
from .views import (
    TransactionListRetrieveViewSet,
    TransactionCreateViewSet,
    BlockListRetrieveViewSet,
    BlockCreateViewSet,
)


# ?router
router = DefaultRouter()
router.register(
    r"transactions", TransactionListRetrieveViewSet, basename="transactions-api"
)
router.register(r"blocks", BlockListRetrieveViewSet, basename="blocks-api")

app_name = "transaction_api"
urlpatterns = [
    path("", include(router.urls)),
    path(
        "transaction/create",
        TransactionCreateViewSet.as_view({"post": "create"}),
        name="transaction-create",
    ),
    path(
        "block/create",
        BlockCreateViewSet.as_view({"post": "create"}),
        name="block-create",
    ),
]
