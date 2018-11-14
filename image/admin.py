from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from image.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    admin.site.empty_value_display = _('Empty')

    def thumb(self, obj):
        if obj.image.image:
            return format_html('<img src="{}" title="{}"', obj.image.image.url, obj.name)

        return obj
    thumb.short_description = _('Image')

    list_display = 'thumb',
    list_display_links = 'thumb',
    list_per_page = 10
