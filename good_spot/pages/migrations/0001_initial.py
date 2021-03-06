# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-29 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
