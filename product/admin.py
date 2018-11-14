from django.contrib import admin

from product.models import Color, Product, ProductImage


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = 'name',


class ProductsImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 0
    raw_id_fields = 'image',


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductsImageAdmin]

    list_display = 'name', 'price', 'old_price', 'promotion', 'stock', 'active',
    list_display_links = 'name',
    list_editable = 'active',
    list_per_page = 10
    search_fields = '=name',
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = 'old_price', 'date',
