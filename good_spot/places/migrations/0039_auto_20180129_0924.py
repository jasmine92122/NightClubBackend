# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-29 09:24
from __future__ import unicode_literals

from django.db import migrations


def add_place_type(apps, schema_editor):
    PlaceType = apps.get_model('places', 'PlaceType')
    PlaceType.objects.create(name="Karaoke", is_active=True, slug='karaoke')


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0038_auto_20180124_1443'),
    ]

    operations = [
        migrations.RunPython(add_place_type),
    ]
