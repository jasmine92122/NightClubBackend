# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0046_actualpopulartimes_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='timezone',
            field=models.CharField(default='UTC', max_length=40),
            preserve_default=False,
        ),
    ]
