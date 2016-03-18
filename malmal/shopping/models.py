from django.db import models


class ShoppingList(models.Model):
    diet = models.ForeignKey('diet.Diet', verbose_name='dieta')
    weekdays = models.ManyToManyField('diet.DietDay',
                                      verbose_name='dni tygodnia')
    datetime_add = models.DateTimeField("data dodania", auto_now_add=True)
    datetime_modified = models.DateTimeField("data ostatnich zmian",
                                             auto_now=True)


class ListItem(models.Model):
    category = models.ForeignKey('product.Category', verbose_name='kategoria')
    product = models.ForeignKey('product.Product', verbose_name='produkt')
    amount = models.FloatField('ilość')
    bought = models.BooleanField('kupione?', default=False)
    datetime_add = models.DateTimeField("data dodania", auto_now_add=True)
    datetime_modified = models.DateTimeField("data ostatnich zmian",
                                             auto_now=True)
