import math

from rest_framework import serializers

from diet.models import Diet
from diet.models import DietDay
from diet.models import Meal
from diet.models import MealItem

from product.models import UNIT_TYPES_MAP
from product.serializers import ProductSerializer


class MealItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    amount_string = serializers.SerializerMethodField()
    amount_pieces = serializers.SerializerMethodField()

    class Meta:
        model = MealItem
        fields = ('id', 'product', 'amount', 'amount_string', 'amount_pieces')

    def get_amount_string(self, meal_item):
        return '{} {}'.format(
            meal_item.amount,
            UNIT_TYPES_MAP[meal_item.product.unit_type])

    def get_amount_pieces(self, meal_item):
        return math.ceil(meal_item.amount / meal_item.product.one_piece_amount)


class MealSerializer(serializers.ModelSerializer):
    meal_items = MealItemSerializer(source='mealitem_set',
                                    read_only=True, many=True)
    time = serializers.DateTimeField(format='%s')

    class Meta:
        model = Meal
        fields = ('id', 'meal_items', 'time')


class DietDaySerializer(serializers.ModelSerializer):
    meals = MealSerializer(source='meal_set', read_only=True, many=True)

    class Meta:
        model = DietDay
        fields = ('id', 'meals', 'weekday')


class DietSerializer(serializers.ModelSerializer):
    days = DietDaySerializer(source='dietday_set', read_only=True, many=True)

    class Meta:
        model = Diet
        fields = ('id', 'days')
