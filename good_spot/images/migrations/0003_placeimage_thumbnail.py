# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-07 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20180306_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeimage',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/', verbose_name='Thumbnail'),
        ),
    ]
