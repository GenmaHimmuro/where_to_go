from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase

from places.models import Organizers, Image


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['image_preview', ]
    extra = 5

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 200px;" />',
                obj.image.url
            )
        return "Нет изображения"


@admin.register(Organizers)
class EventAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title', 'id', ]
    search_fields = ['title', ]
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['organizer', 'ordinal_number',]
    list_editable = ['ordinal_number', ]
    search_fields = ['organizer',]
