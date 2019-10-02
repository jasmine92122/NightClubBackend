# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0045_remove_place_actual_populartimes'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualpopulartimes',
            name='place',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='places.Place'),
            preserve_default=False,
        ),
    ]