from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from diet.models import WEEKDAYS_MAP
from product.models import UNIT_TYPES_MAP

from fridge.models import FridgeItem


class ShoppingList(models.Model):
    diet = models.ForeignKey('diet.Diet', verbose_name='dieta')
    weekdays = models.ManyToManyField('diet.DietDay',
                                      verbose_name='dni tygodnia')
    datetime_add = models.DateTimeField("data dodania", auto_now_add=True)
    datetime_modified = models.DateTimeField("data ostatnich zmian",
                                             auto_now=True)
    done = models.BooleanField('zrobione?', default=False)

    def __str__(self):
        return 'ShoppingList: {} for {}'.format(
            self.diet,
            ', '.join(WEEKDAYS_MAP[d.weekday] for d in self.weekdays.all()))


@receiver(post_save, sender=ShoppingList)
def update_fridge(sender, instance, created, **kwargs):
    if instance.done:
        # BUG(sylwek): will be generated everytime shopping list is saved,
        # must be fixed.
        fridge = instance.diet.fridge_set.first()
        for listitem in instance.listitem_set.filter(bought=True):
            product = listitem.product
            fridgeitem = fridge.fridgeitem_set.filter(product=product).first()
            if fridgeitem is not None:
                fridgeitem.amount += listitem.amount
                fridgeitem.save()
            else:
                FridgeItem.objects.create(
                    category=product.category,
                    product=product,
                    amount=listitem.amount)


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
