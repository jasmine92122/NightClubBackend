# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-20 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0054_place_populartimes_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Do you want to show this city in dropdown menu in app?', verbose_name='Active?'),
        ),
    ]
