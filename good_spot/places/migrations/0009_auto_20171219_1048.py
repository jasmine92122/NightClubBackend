# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 10:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_place_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='google_rating',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(1.0)]),
        ),
    ]
