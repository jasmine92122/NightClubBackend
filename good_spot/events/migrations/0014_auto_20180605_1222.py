# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-05 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20180601_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatingrule',
            name='start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Time to update'),
        ),
    ]