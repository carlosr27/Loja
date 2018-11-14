from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from home.models import BannerTop, BannerTopImage, BannerBottom


@admin.register(BannerBottom)
class BannerBottomAdmin(admin.ModelAdmin):
    admin.site.empty_value_display = _('Empty')

    def thumb(self, obj):
        if obj.image.image:
            return format_html('<img src="{}" title="{}"', obj.image.image.url, obj.name)

        return obj
    thumb.short_description = _('Image')

    list_display = 'thumb', 'position', 'link', 'active', 'date'
    list_display_links = 'thumb',
    list_editable = 'active',
    list_filter = 'date',
    list_per_page = 40
    readonly_fields = 'date',


class BannerTopImage(admin.TabularInline):
    model = BannerTopImage
    extra = 0


@admin.register(BannerTop)
class BannerTopAdmin(admin.ModelAdmin):
    admin.site.empty_value_display = _('Empty')

    # def thumb(self, obj):
    #     if obj.image.image:
    #         return format_html('<img src="{}" title="{}"', obj.image.image.url, obj.name)
    #
    #     return obj
    # thumb.short_description = _('Image')

    inlines = [BannerTopImage]
    list_display = 'group_position',  'active', 'date'
    # list_display_links = 'thumb',
    list_editable = 'active',
    list_filter = 'date',
    list_per_page = 40
    readonly_fields = 'date',
