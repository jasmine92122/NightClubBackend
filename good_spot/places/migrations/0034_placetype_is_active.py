# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-24 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0033_auto_20180124_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='placetype',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Show in app.', verbose_name='Is active?'),
        ),
    ]
