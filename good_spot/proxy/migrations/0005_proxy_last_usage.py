# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-16 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0004_auto_20180212_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='proxy',
            name='last_usage',
            field=models.DateTimeField(auto_now_add=True, default='2018-02-16 10:32:54.448657+00:00'),
            preserve_default=False,
        ),
    ]
