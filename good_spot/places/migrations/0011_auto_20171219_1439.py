# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_auto_20171219_1217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AddField(
            model_name='placetype',
            name='slug',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Google type'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_types',
            field=models.ManyToManyField(blank=True, to='places.PlaceType'),
        ),
    ]
