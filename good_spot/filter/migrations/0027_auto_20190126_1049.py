# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-26 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0026_auto_20180926_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterfield',
            name='is_shown_in_features',
            field=models.BooleanField(default=False, help_text='Use this field to generate features displaying under the title of place.', verbose_name='Title: Bold Upper part of short description'),
        ),
        migrations.AlterField(
            model_name='filterfield',
            name='is_shown_in_short_description',
            field=models.BooleanField(default=False, help_text='Use this field to generate `Short Description` section on detail screen.', verbose_name='Sub title: Sub part of short description'),
        ),
    ]
