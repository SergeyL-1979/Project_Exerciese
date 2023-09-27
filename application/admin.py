from django.contrib import admin

from application.models import Product, ProductAccess


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "user", ]


@admin.register(ProductAccess)
class ProductAccessAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "is_valid"]
