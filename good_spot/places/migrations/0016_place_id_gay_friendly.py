# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_place_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='id_gay_friendly',
            field=models.BooleanField(default=False),
        ),
    ]