2018-03-30
Translations
Added fields for translation:
- good_spot.places.models.Place
    -   name, address, special_event
- good_spot.places.models.PlaceType
    -   name
- good_spot.filter.models.FilterField
    -   name
- good_spot.filter.models.ChoiceFilterFieldOption
    -   option
- good_spot.filter.models.PlaceTextFilterField
    -   value
- cities_light.models.Country
    -   name
- cities_light.models.City
    -   name


2018-03-28
Migrated filters and relations with places to a new `filter` application.
Overridden M2M relations to show only appropriate choices for each field type.


2018-03-27

Created polymorphic models in `filter` application instead of good_spot.filter.PlaceField
Created admin inlines for new polymorphic models. Customized formset moved and adapted to new inline. Customized template so three inlines looks like one inline.


2018-03-26

Customized inline FilterFieldInline. Overridden formset and methods of this inline.
The reason - make inline easier. Filter fields prepopulated by all available option. 
Admin should just choose values.