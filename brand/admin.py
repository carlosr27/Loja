from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


from brand.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    admin.site.empty_value_display = _('Empty')

    def thumb(self, obj):
        if obj.image.image:
            return format_html('<img src="{}" title="{}"', obj.image.image.url, obj.name)

        return obj
    thumb.short_description = _('Image')

    list_display = 'name', 'slug', 'thumb', 'active', 'date'
    list_editable = 'active',
    list_filter = 'date',
    list_per_page = 30
    search_fields = '=name',
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = 'date',
