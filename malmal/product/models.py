from django.db import models


class Category(models.Model):
    name = models.CharField('nazwa', max_length=100)

    def __str__(self):
        return 'Category: {}'.format(self.name)


UNIT_TYPES = (
    ('volume', 'Objętość'),
    ('mass', 'Waga'),
)

UNIT_TYPES_MAP = {
    'volume': 'ml',
    'mass': 'g',
}


class Product(models.Model):
    name = models.CharField('nazwa', max_length=100)
    category = models.ForeignKey(Category, verbose_name='kategoria',
                                 related_name='products')
    unit_type = models.CharField('typ jednostki', max_length=40,
                                 choices=UNIT_TYPES)
    # every value is per 100g
    proteins = models.FloatField('białko', help_text='na 100g')
    carbo = models.FloatField('węglowodany', help_text='na 100g')
    fat = models.FloatField('tłuszcze', help_text='na 100g')
    one_piece_amount = models.FloatField('ilość jednej sztuki',
                                         help_text='np 150g to 1 sztuka')

    def __str__(self):
        return 'Product: {} ({})'.format(self.name, self.category.name)
