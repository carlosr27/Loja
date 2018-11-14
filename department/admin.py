from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


from department.models import Category, Collection, Department, SubCategory


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     admin.site.empty_value_display = _('Empty')
#
#     list_display = 'name', 'slug', 'department', 'active',
#     list_display_links = 'name',
#     list_editable = 'active',
#     list_filter = 'department',
#     list_per_page = 30,
#     search_fields = '=name',
#     prepopulated_fields = {'slug': ('name',)}
#
#
# @admin.register(Collection)
# class CollectionAdmin(admin.ModelAdmin):
#     admin.site.empty_value_display = _('Empty')
#
#     list_display = 'name', 'slug', 'sub_category', 'home', 'active',
#     list_display_links = 'name',
#     list_editable = 'active', 'home',
#     list_filter = 'sub_category',
#     list_per_page = 30,
#     filter_horizontal = 'sub_category',
#     search_fields = '=name',
#     prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.TabularInline):
    model = Category
    extra = 0


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    admin.site.empty_value_display = _('Empty')

    inlines = [CategoryAdmin]

    def thumb(self, obj):
        if obj.image.image:
            return format_html('<img src="{}" title="{}"', obj.image.image.url, obj.name)

        return obj
    thumb.short_description = _('Image')

    list_display = 'name', 'thumb',
    list_display_links = 'name',


# @admin.register(SubCategory)
# class SubCategoryAdmin(admin.ModelAdmin):
#     admin.site.empty_value_display = _('Empty')
#
#     list_display = 'name', 'slug', 'category', 'active'
#     list_display_links = 'name',
#     list_editable = 'active',
#     list_filter = 'category',
#     list_per_page = 30,
#     search_fields = '=name',
#     prepopulated_fields = {'slug': ('name',)}
