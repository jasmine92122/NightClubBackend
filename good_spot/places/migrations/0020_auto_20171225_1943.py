# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0019_place_google_price_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Website'),
        ),
    ]
