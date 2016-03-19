import math
from rest_framework import serializers

from product.models import UNIT_TYPES_MAP
from product.serializers import ProductSerializer

from shopping.models import ListItem
from shopping.models import ShoppingList


class ListItemSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    product = ProductSerializer(read_only=True)
    amount_string = serializers.SerializerMethodField()
    amount_pieces = serializers.SerializerMethodField()

    class Meta:
        model = ListItem
        fields = ('id', 'category', 'product', 'amount', 'amount_string',
                  'amount_pieces', 'bought')

    def get_amount_string(self, meal_item):
        return '{} {}'.format(
            meal_item.amount,
            UNIT_TYPES_MAP[meal_item.product.unit_type])

    def get_amount_pieces(self, meal_item):
        return math.ceil(meal_item.amount / meal_item.product.one_piece_amount)


class ShoppingListSerializer(serializers.ModelSerializer):
    list_items = ListItemSerializer(source='listitem_set', many=True)
    weekdays = serializers.SerializerMethodField()

    def get_weekdays(self, shopping_list):
        return [d.weekday for d in shopping_list.weekdays.all()]

    class Meta:
        model = ShoppingList
        fields = ('id', 'weekdays', 'diet', 'list_items', 'done')


class CompareFridgeSerializer(serializers.ModelSerializer):
    diet = serializers.IntegerField(source='diet.pk')
    list_items = serializers.SerializerMethodField()

    def get_list_items(self, shopping_list):
        fridge = shopping_list.diet.fridge_set.first()
        items_to_check = []
        for listitem in shopping_list.listitem_set.all():
            product = listitem.product
            fridgeitem = fridge.fridgeitem_set.filter(product=product).first()
            if fridgeitem is not None:
                ask_about = 0
                if fridgeitem.amount - listitem.amount >= 0:
                    ask_about = listitem.amount
                elif fridgeitem.amount - listitem.amount < 0:
                    ask_about = fridgeitem.amount

                if ask_about == 0:
                    listitem.delete()
                else:
                    listitem.amount = ask_about
                    items_to_check.append(listitem)

        return [ListItemSerializer(item).data for item in items_to_check]

    class Meta:
        model = ShoppingList
        fields = ('id', 'diet', 'list_items')


class FridgeStatusSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    lack = serializers.BooleanField()
