# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-30 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20180530_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(choices=[('terms', 'terms'), ('policy', 'policy')], max_length=6, unique=True),
        ),
    ]
