from django.contrib import admin

from lesson.models import Lesson, LessonInfo


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["title", "url_link", "video_duration", ]


@admin.register(LessonInfo)
class LessonInfoAdmin(admin.ModelAdmin):
    list_display = ["lesson", "user", "status", "video_view", ]


