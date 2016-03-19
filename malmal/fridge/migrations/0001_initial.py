# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0003_auto_20160318_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_add', models.DateTimeField(auto_now_add=True, verbose_name='data dodania')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='data ostatnich zmian')),
            ],
        ),
        migrations.CreateModel(
            name='FridgeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='ilość')),
                ('lack', models.BooleanField(default=False, verbose_name='brak?')),
                ('datetime_add', models.DateTimeField(auto_now_add=True, verbose_name='data dodania')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='data ostatnich zmian')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='kategoria')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='produkt')),
            ],
        ),
    ]