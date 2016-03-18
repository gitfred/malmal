from django.db import models

from product.models import UNIT_TYPES_MAP


class Diet(models.Model):
    datetime_add = models.DateTimeField("data dodania", auto_now_add=True)
    datetime_modified = models.DateTimeField("data ostatnich zmian",
                                             auto_now=True)

    def __str__(self):
        return 'Diet: {}'.format(self.pk)


WEEKDAYS = (
    ('1', 'Poniedziałek'),
    ('2', 'Wtorek'),
    ('3', 'Środa'),
    ('4', 'Czwartek'),
    ('5', 'Piątek'),
    ('6', 'Sobota'),
    ('7', 'Niedziela'),
)

WEEKDAYS_MAP = dict(WEEKDAYS)


class DietDay(models.Model):
    diet = models.ForeignKey(Diet, verbose_name='dieta')
    weekday = models.CharField('dzień tygodnia', max_length=20,
                               choices=WEEKDAYS)
    datetime_add = models.DateTimeField("data dodania", auto_now_add=True)
    datetime_modified = models.DateTimeField("data ostatnich zmian",
                                             auto_now=True)

    def __str__(self):
        return 'Day: {} ({})'.format(WEEKDAYS_MAP[self.weekday], self.diet.pk)


class Meal(models.Model):
    name = models.CharField('nazwa', max_length=100, null=True, blank=True)
    day = models.ForeignKey(DietDay, verbose_name='dzień diety')
    time = models.TimeField('czas posiłku')
    recipe = models.TextField('przepis', null=True, blank=True)

    def __str__(self):
        return 'Meal: {} ({})'.format(self.name, WEEKDAYS_MAP[self.day.weekday])


class MealItem(models.Model):
    meal = models.ForeignKey(Meal, verbose_name='posiłek')
    product = models.ForeignKey('product.Product', verbose_name='product')
    amount = models.FloatField('ilość')

    def __str__(self):
        return 'MealItem: {} ({} {})'.format(
            self.product.name, self.amount,
            UNIT_TYPES_MAP[self.product.unit_type])
