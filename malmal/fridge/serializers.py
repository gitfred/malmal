import math
from rest_framework import serializers

from product.models import UNIT_TYPES_MAP
from product.serializers import ProductSerializer

from fridge.models import FridgeItem
from fridge.models import Fridge


class FridgeItemSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    product = ProductSerializer(read_only=True)
    amount_string = serializers.SerializerMethodField()
    amount_pieces = serializers.SerializerMethodField()

    class Meta:
        model = FridgeItem
        fields = ('id', 'category', 'product', 'amount', 'amount_string',
                  'amount_pieces', 'lack')

    def get_amount_string(self, meal_item):
        return '{} {}'.format(
            meal_item.amount,
            UNIT_TYPES_MAP[meal_item.product.unit_type])

    def get_amount_pieces(self, meal_item):
        return math.ceil(meal_item.amount / meal_item.product.one_piece_amount)


class FridgeSerializer(serializers.ModelSerializer):
    diet = serializers.IntegerField(source='diet.pk')
    fridge_items = FridgeItemSerializer(source='fridgeitem_set', many=True)

    class Meta:
        model = Fridge
        fields = ('id', 'diet', 'fridge_items')
