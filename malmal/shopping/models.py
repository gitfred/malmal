from django.db import models

from diet.models import WEEKDAYS_MAP
from product.models import UNIT_TYPES_MAP


class ShoppingList(models.Model):
    diet = models.ForeignKey('diet.Diet', verbose_name='dieta')
    weekdays = models.ManyToManyField('diet.DietDay',
                                      verbose_name='dni tygodnia')
    datetime_add = models.DateTimeField("data dodania", auto_now_add=True)
    datetime_modified = models.DateTimeField("data ostatnich zmian",
                                             auto_now=True)

    def __str__(self):
        return 'ShoppingList: {} for {}'.format(
            self.diet,
            ', '.join(WEEKDAYS_MAP[d.weekday] for d in self.weekdays.all()))


class ListItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, verbose_name='lista')
    category = models.ForeignKey('product.Category', verbose_name='kategoria')
    product = models.ForeignKey('product.Product', verbose_name='produkt')
    amount = models.FloatField('ilość')
    bought = models.BooleanField('kupione?', default=False)
    datetime_add = models.DateTimeField("data dodania", auto_now_add=True)
    datetime_modified = models.DateTimeField("data ostatnich zmian",
                                             auto_now=True)

    def __str__(self):
        return 'ListItem: {} ({} {})'.format(
            self.product.name, self.amount,
            UNIT_TYPES_MAP[self.product.unit_type])
