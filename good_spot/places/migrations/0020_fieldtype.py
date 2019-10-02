# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-24 14:54
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0019_place_google_price_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('field_type', models.CharField(max_length=6, verbose_name='Type')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Choices')),
                ('is_public', models.BooleanField(default=True, verbose_name='Is public?')),
                ('is_filter', models.BooleanField(default=False, verbose_name='Is filter?')),
                ('is_shown_in_short_description', models.BooleanField(default=False, verbose_name='Show in short description')),
                ('is_disabled', models.BooleanField(default=False, verbose_name='Is disabled?')),
                ('place_type', models.ManyToManyField(to='places.PlaceType')),
            ],
        ),
    ]
