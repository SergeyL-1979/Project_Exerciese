from django.contrib import admin

from application.models import Product, Lesson


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name_product", "author_product", ]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["lesson_name", "lesson_link", "lesson_time", ]
    # readonly_fields = ["lesson_prod"]

