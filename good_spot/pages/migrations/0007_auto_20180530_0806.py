# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-30 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20180530_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.CharField(choices=[('terms', 'terms'), ('policy', 'policy')], max_length=6, unique=True),
        ),
    ]
