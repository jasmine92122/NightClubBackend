# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-12 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import good_spot.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_placeimage_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(upload_to=good_spot.images.models.user_directory_path, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='resized-images/', verbose_name='Thumbnail'),
        ),
    ]
