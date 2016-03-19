from django.contrib import admin

from fridge.models import Fridge
from fridge.models import FridgeItem


@admin.register(Fridge)
class FridgeAdmin(admin.ModelAdmin):
    pass


@admin.register(FridgeItem)
class FridgeItemAdmin(admin.ModelAdmin):
    pass
