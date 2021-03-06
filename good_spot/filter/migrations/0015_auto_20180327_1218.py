# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-27 12:18
from __future__ import unicode_literals

from django.db import migrations


from structlog import get_logger

log = get_logger()


def migrate_filters(apps, schema_editor):
    from django.contrib.contenttypes.models import ContentType

    FilterField = apps.get_model('filter', 'FilterField')
    FilterField.objects.all().delete()

    BoolFilterField = apps.get_model('filter', 'BoolFilterField')
    TextFilterField = apps.get_model('filter', 'TextFilterField')
    ChoiceFilterField = apps.get_model('filter', 'ChoiceFilterField')
    ChoiceFilterFieldOption = apps.get_model('filter', 'ChoiceFilterFieldOption')

    PlaceFilterField = apps.get_model('filter', 'PlaceFilterField')
    PlaceFilterField.objects.all().delete()

    PlaceChoiceFilterField = apps.get_model('filter', 'PlaceChoiceFilterField')
    PlaceBoolFilterField = apps.get_model('filter', 'PlaceBoolFilterField')
    PlaceTextFilterField = apps.get_model('filter', 'PlaceTextFilterField')

    FieldType = apps.get_model('places', 'FieldType')

    for field in FieldType.objects.all():

        if field.field_type == 'bool':
            ct = ContentType.objects.get_for_model(BoolFilterField)
            new_field = BoolFilterField.objects.create(
                polymorphic_ctype_id=ct.id,
                name=field.name,
                is_public=field.is_public,
                is_filter=field.is_filter,
                is_shown_in_features=field.is_shown_in_features,
                is_shown_in_short_description=field.is_shown_in_short_description,
                is_shown_in_about_place=field.is_shown_in_about_place,
                order=field.order
            )
            new_field.place_type.add(*field.place_type.all())

            for place_field in field.place_fields.all():
                ctype = ContentType.objects.get_for_model(PlaceBoolFilterField)
                PlaceBoolFilterField.objects.create(
                    polymorphic_ctype_id=ctype.id,
                    place=place_field.place,
                    field_type=new_field,
                    value=place_field.value
                )

        elif field.field_type == 'text':
            ct = ContentType.objects.get_for_model(TextFilterField)
            new_field = TextFilterField.objects.create(
                polymorphic_ctype_id=ct.id,
                name=field.name,
                is_public=field.is_public,
                is_filter=field.is_filter,
                is_shown_in_features=field.is_shown_in_features,
                is_shown_in_short_description=field.is_shown_in_short_description,
                is_shown_in_about_place=field.is_shown_in_about_place,
                order=field.order
            )
            new_field.place_type.add(*field.place_type.all())

            for place_field in field.place_fields.all():
                ctype = ContentType.objects.get_for_model(PlaceTextFilterField)
                PlaceTextFilterField.objects.create(
                    polymorphic_ctype_id=ctype.id,
                    place=place_field.place,
                    field_type=new_field,
                    value=place_field.value
                )

        elif field.field_type == 'choice':
            ct = ContentType.objects.get_for_model(ChoiceFilterField)
            new_field = ChoiceFilterField.objects.create(
                polymorphic_ctype_id=ct.id,
                name=field.name,
                is_public=field.is_public,
                is_filter=field.is_filter,
                is_shown_in_features=field.is_shown_in_features,
                is_shown_in_short_description=field.is_shown_in_short_description,
                is_shown_in_about_place=field.is_shown_in_about_place,
                order=field.order
            )
            new_field.place_type.add(*field.place_type.all())

        elif field.field_type == 'multi':
            ct = ContentType.objects.get_for_model(ChoiceFilterField)
            new_field = ChoiceFilterField.objects.create(
                polymorphic_ctype_id=ct.id,
                name=field.name,
                is_multi=True,
                is_public=field.is_public,
                is_filter=field.is_filter,
                is_shown_in_features=field.is_shown_in_features,
                is_shown_in_short_description=field.is_shown_in_short_description,
                is_shown_in_about_place=field.is_shown_in_about_place,
                order=field.order
            )
            new_field.place_type.add(*field.place_type.all())

        # Migrating list of choices for select
        if field.field_type in ['choice', 'multi']:
            for option in field.data:
                if not ChoiceFilterFieldOption.objects.filter(
                    choice_filter_field = new_field,
                    option=option
                ).exists():
                    ChoiceFilterFieldOption.objects.create(
                        choice_filter_field = new_field,
                        option=option
                    )

            # Migrating places for field
            for place_field in field.place_fields.all():
                ctype = ContentType.objects.get_for_model(PlaceChoiceFilterField)
                new_place_field = PlaceChoiceFilterField.objects.create(
                    polymorphic_ctype_id=ctype.id,
                    place=place_field.place,
                    field_type=new_field
                )

                for opt in place_field.value:
                    ch_opt = ChoiceFilterFieldOption.objects.filter(
                        choice_filter_field=new_field,
                        option=opt
                    ).first()
                    if ch_opt:
                        new_place_field.value.add(ch_opt)
                    else:
                        log.error("Error when try to create new option `{}` from place_field={}".format(
                            opt,
                            place_field.id
                        ))


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0014_placetextfilterfield'),
    ]

    operations = [
        migrations.RunPython(migrate_filters)
    ]
