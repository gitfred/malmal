from django.contrib import admin

from product.models import Category
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
