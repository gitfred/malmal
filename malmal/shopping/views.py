from rest_framework import viewsets
from rest_framework import response
from rest_framework import generics

from shopping.models import ShoppingList
from shopping.serializers import ShoppingListSerializer
from shopping.serializers import CompareFridgeSerializer


class ShoppingListViewSet(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class CompareFridgeListView(generics.RetrieveAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = CompareFridgeSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        shopping_list = self.get_object()
        fridge = shopping_list.diet.fridge_set.first()
        for item in data:
            if item['lack'] is False:
                continue
            listitem = shopping_list.listitem_set.filter(id=item['id']).first()
            product = listitem.product
            fridgeitem = fridge.fridgeitem_set.filter(product=product).first()

            if fridgeitem.amount - listitem.amount >= 0:
                listitem.delete()
            elif fridgeitem.amount - listitem.amount < 0:
                listitem.amount -= fridgeitem.amount
                listitem.save()

        return response.Response(
            ShoppingListSerializer(shopping_list).data, status=200)

