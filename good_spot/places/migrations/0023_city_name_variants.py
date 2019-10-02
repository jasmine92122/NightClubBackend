# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 12:02
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0022_auto_20171227_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='name_variants',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
