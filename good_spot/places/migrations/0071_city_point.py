# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-02 11:36
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0070_auto_20180330_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]