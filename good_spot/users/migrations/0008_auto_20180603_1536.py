# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-03 15:36
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180603_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='users/avatars'),
        ),
    ]
