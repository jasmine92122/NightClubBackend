# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 08:57
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0021_merge_20171227_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='extended_place_types',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]