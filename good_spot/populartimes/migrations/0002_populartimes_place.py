# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-03 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0073_auto_20180402_1158'),
        ('populartimes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='populartimes',
            name='place',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='place_poptimes', to='places.Place'),
            preserve_default=False,
        ),
    ]
