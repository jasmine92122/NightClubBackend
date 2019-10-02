# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-30 08:15
from __future__ import unicode_literals

from django.core import management
from django.db import migrations


def populate_pages(apps, schema_editor):
    Page = apps.get_model('pages', 'Page')
    # creating Terms and Conds
    Page.objects.create(
        title='Terms and Conditions',
        slug='terms',
        text=' '
    )
    # creating Policy
    Page.objects.create(
        title='Privacy Policy',
        slug='policy',
        text=' '
    )

class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_page_is_published'),
    ]

    operations = [
        migrations.RunPython(populate_pages),
    ]
