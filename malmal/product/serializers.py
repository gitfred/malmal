from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'proteins', 'carbo', 'fat')
