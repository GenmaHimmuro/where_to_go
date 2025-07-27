from django.contrib import admin
from places.models import Organizers, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Organizers)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', ]
    search_fields = ['title', ]
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['organizer',]
    search_fields = ['organizer',]