from django.contrib import admin
from .models import Pickup, LineText, FavoritePickup, Like

# Register your models here.

admin.site.register(Pickup)
admin.site.register(LineText)
admin.site.register(FavoritePickup)
admin.site.register(Like)
