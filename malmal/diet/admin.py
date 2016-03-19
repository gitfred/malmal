from django.contrib import admin

from diet.models import Diet
from diet.models import DietDay
from diet.models import Meal
from diet.models import MealItem


@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    pass


@admin.register(DietDay)
class DietDayAdmin(admin.ModelAdmin):
    pass


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    pass


@admin.register(MealItem)
class MealItemAdmin(admin.ModelAdmin):
    pass
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "product":
    #         kwargs["queryset"] = MealItem.objects.order_by('product__name')
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
