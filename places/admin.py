from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase

from places.models import Organizers, Image


MAX_HEIGHT_IMG = 200
MAX_WIDTH_IMG = 200


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['image_preview', ]
    extra = 5

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                f'<img src="{{}}" style="max-height: {MAX_HEIGHT_IMG}px; max-width: {MAX_WIDTH_IMG}px;" />',
                obj.image.url
            )
        return 'Нет изображения'


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
    autocomplete_fields = ['organizer', ]
