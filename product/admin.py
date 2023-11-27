from django.contrib import admin
from django.utils.html import format_html

from product.form import ColorForm
from product.models import Product, Category, Size, Tag, Color, Brand, WishList


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_active')
    readonly_fields = ['real_price']
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'color_preview')
    list_filter = ('is_active',)
    search_fields = ('name',)
    form = ColorForm

    def color_preview(self, obj):
        return format_html(
            f'<div style=\"width: 30px; height: 30px; border-radius:50px; background-color: {obj}"></div>',
            obj.name,
        )

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    list_filter = ('user', 'product')
    search_fields = ('user', 'product')