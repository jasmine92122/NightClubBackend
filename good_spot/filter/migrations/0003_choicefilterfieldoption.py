# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0002_boolfilterfield_choicefilterfield_textfilterfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceFilterFieldOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('option', models.CharField(max_length=100)),
                ('choice_filter_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filter.ChoiceFilterField')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]