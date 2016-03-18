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
