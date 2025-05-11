from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class PhotosInline(admin.TabularInline):
    model = Photos
    extra = 1


@admin.register(Property)
class BaseApartmentAdmin(TranslationAdmin):
    inlines = [PhotosInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
# admin.site.register(Property)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Photos)
# admin.site.register()
