from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Product
        fields = ('id', 'category', 'proteins', 'carbo', 'fat')
