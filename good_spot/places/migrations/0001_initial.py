# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Place type')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Icon')),
            ],
        ),
    ]
