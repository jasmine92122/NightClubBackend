# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-11 07:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0077_placetype_active_in_cities'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Application cities'},
        ),
    ]