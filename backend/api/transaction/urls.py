# Django
from django.urls import path, include

# Django Rest
from rest_framework.routers import DefaultRouter

# Views,Model,Serializers
from .views import TransactionListRetrieveViewSet


# ?router
router = DefaultRouter()
router.register(
    r"transactions", TransactionListRetrieveViewSet, basename="transactions-api"
)


app_name = "transaction_api"
urlpatterns = [path("", include(router.urls))]
