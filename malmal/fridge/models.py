from django.db import models


from product.models import UNIT_TYPES_MAP


class Fridge(models.Model):
    diet = models.ForeignKey('diet.Diet', verbose_name='dieta')
    datetime_add = models.DateTimeField("data dodania", auto_now_add=True)
    datetime_modified = models.DateTimeField("data ostatnich zmian",
                                             auto_now=True)

    def __str__(self):
        return 'Fridge: {}'.format(self.pk)


class FridgeItem(models.Model):
    category = models.ForeignKey('product.Category', verbose_name='kategoria')
    product = models.ForeignKey('product.Product', verbose_name='produkt')
    fridge = models.ForeignKey(Fridge, verbose_name='lodówka')
    amount = models.FloatField('ilość')
    lack = models.BooleanField('brak?', default=False)
    datetime_add = models.DateTimeField("data dodania", auto_now_add=True)
    datetime_modified = models.DateTimeField("data ostatnich zmian",
                                             auto_now=True)

    def __str__(self):
        return 'FridgeItem: {} ({} {})'.format(
            self.product.name, self.amount,
            UNIT_TYPES_MAP[self.product.unit_type])
