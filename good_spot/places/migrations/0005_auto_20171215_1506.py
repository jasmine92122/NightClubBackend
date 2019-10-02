# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 15:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20171215_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='google_rating',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)]),
        ),
    ]
