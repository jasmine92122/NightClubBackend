# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-06 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
        ('places', '0049_auto_20180131_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.RemoveField(
            model_name='city',
            name='name',
        ),
        migrations.AddField(
            model_name='city',
            name='city',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.City'),
        ),
        migrations.AlterField(
            model_name='place',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.City'),
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
