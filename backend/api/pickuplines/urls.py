#Django
from django.urls import path,include
from .views import *

#Django Rest
from rest_framework.routers import DefaultRouter



#?router
router = DefaultRouter()
router.register(r"users",TestViewSet,basename='users-api')


#?urlpatterns
app_name='pickuplines_api'
urlpatterns = [
    path('',include(router.urls))
]