# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-28 07:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0060_auto_20180313_0938'),
        ('filter', '0015_auto_20180327_1218'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='placefield',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='placefield',
            name='field_type',
        ),
        migrations.RemoveField(
            model_name='placefield',
            name='place',
        ),
        migrations.RemoveField(
            model_name='placefield',
            name='value',
        ),
        migrations.AlterField(
            model_name='placefilterfield',
            name='field_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_filter_field', to='filter.FilterField'),
        ),
        migrations.AlterField(
            model_name='placefilterfield',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_filter_field', to='places.Place'),
        ),
        migrations.AlterUniqueTogether(
            name='placefilterfield',
            unique_together=set([('place', 'field_type')]),
        ),
        migrations.DeleteModel(
            name='PlaceField',
        ),
    ]
