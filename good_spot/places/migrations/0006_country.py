# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20171215_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Country name')),
                ('code', models.CharField(help_text='ISO Alpha-2 Code', max_length=2, unique=True, verbose_name='Country code')),
            ],
        ),
    ]
