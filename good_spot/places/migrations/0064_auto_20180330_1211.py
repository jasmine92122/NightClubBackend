# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-30 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0063_auto_20180330_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='name',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
    ]