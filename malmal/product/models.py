from django.db import models


class Category(models.Model):
    name = models.CharField('nazwa', max_length=100)


UNIT_TYPES = (
    ('volume', 'Objętość'),
    ('mass', 'Waga'),
)


class Product(models.Model):
    name = models.CharField('nazwa', max_length=100)
    category = models.ForeignKey(Category, verbose_name='kategoria',
                                 related_name='products')
    unit_type = models.CharField('typ jednostki', max_length=40,
                                 choices=UNIT_TYPES)
    # every value is per 100g
    proteins = models.FloatField('białko')
    carbo = models.FloatField('węglowodany')
    fat = models.FloatField('tłuszcze')
