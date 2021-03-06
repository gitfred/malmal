# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0001_initial'),
        ('fridge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fridge',
            name='diet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='diet.Diet', verbose_name='dieta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fridgeitem',
            name='fridge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fridge.Fridge', verbose_name='lodówka'),
            preserve_default=False,
        ),
    ]
