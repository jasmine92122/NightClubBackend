# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-29 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0027_auto_20171229_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldtype',
            name='is_shown_in_about_place',
            field=models.BooleanField(default=False, verbose_name='Show in About Place section'),
        ),
    ]
