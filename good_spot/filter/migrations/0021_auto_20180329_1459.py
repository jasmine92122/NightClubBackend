# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-29 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0020_auto_20180329_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='placetextfilterfield',
            name='value_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='placetextfilterfield',
            name='value_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='placetextfilterfield',
            name='value_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='placetextfilterfield',
            name='value_uk',
            field=models.CharField(max_length=255, null=True),
        ),
    ]