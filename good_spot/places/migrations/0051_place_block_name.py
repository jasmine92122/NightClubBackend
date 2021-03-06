# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-09 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0050_auto_20180206_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='block_name',
            field=models.BooleanField(default=False, help_text="Block <b>Place types</b> from updating from the Google Places API.<br>It means, if you change <b>Place types</b> manually, it won't be rewritten from the Google Places API after updating."),
        ),
    ]
