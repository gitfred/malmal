from rest_framework import viewsets

from shopping.models import ShoppingList
from shopping.serializers import ShoppingListSerializer


class ShoppingListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
