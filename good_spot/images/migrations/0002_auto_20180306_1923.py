# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-06 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Image'),
        ),
    ]
