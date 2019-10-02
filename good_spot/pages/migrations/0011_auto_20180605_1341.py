# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-05 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20180605_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.CharField(choices=[('terms', 'terms'), ('policy', 'policy'), ('faq', 'faq')], max_length=6, unique=True),
        ),
    ]