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
        fields = ('id', 'weekdays', 'diet', 'list_items')
