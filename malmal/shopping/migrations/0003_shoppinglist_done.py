# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_listitem_shopping_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='done',
            field=models.BooleanField(default=False, verbose_name='zrobione?'),
        ),
    ]
