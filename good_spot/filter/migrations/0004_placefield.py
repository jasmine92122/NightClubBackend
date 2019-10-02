# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0060_auto_20180313_0938'),
        ('filter', '0003_choicefilterfieldoption'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('field_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_filter_fields', to='filter.FilterField')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_filter_fields', to='places.Place')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
