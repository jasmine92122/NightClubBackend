# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-06 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0075_merge_20180601_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='website',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Website'),
        ),
    ]