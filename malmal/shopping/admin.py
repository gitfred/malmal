from django.contrib import admin

from shopping.models import ListItem
from shopping.models import ShoppingList


@admin.register(ListItem)
class ListItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    pass
