# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-13 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0086_auto_20180813_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placetype',
            name='name_plural',
            field=models.CharField(blank=True, max_length=20, verbose_name='Place type (plural)'),
        ),
        migrations.AlterField(
            model_name='placetype',
            name='name_plural_en',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Place type (plural)'),
        ),
        migrations.AlterField(
            model_name='placetype',
            name='name_plural_fr',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Place type (plural)'),
        ),
        migrations.AlterField(
            model_name='placetype',
            name='name_plural_ru',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Place type (plural)'),
        ),
        migrations.AlterField(
            model_name='placetype',
            name='name_plural_uk',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Place type (plural)'),
        ),
    ]