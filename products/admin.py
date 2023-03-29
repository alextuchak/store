from django.contrib import admin

from products.models import Basket, ProductCategory, Products, ProductsGallery

admin.site.register(ProductCategory)
admin.site.register(ProductsGallery)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ['name', 'descriptions', 'full_descriptions', 'manufacturer', 'price', 'quantity', 'image', 'category']
    readonly_fields = []
    search_fields = ['name']
    ordering = ['name']


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_at')
    readonly_fields = ('created_at',)
    extra = 0
