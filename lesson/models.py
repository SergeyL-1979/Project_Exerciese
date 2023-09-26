from django.db import models

from application.models import Product
from users.models import User


class Lesson(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название урока')
    url_link = models.URLField(null=True, blank=True, verbose_name='URL на урок')
    video_duration = models.PositiveIntegerField(default=0, verbose_name='Продолжительность')
    products = models.ManyToManyField(Product)


class LessonStatus(models.TextChoices):
    VIEWED = "Просмотрено"
    NOT_VIEWED = "Не просмотрено"


class LessonInfo(models.Model):
    lesson = models.ForeignKey(Lesson, models.CASCADE, related_name='views')
    user = models.ForeignKey(User, models.CASCADE)
    status = models.CharField(max_length=30, choices=LessonStatus.choices, default=LessonStatus.NOT_VIEWED)
    video_view = models.PositiveIntegerField(default=0)




# class Lesson(models.Model):
#     """
#     2. Создать сущность урока. Урок может находиться в нескольких продуктах одновременно.
#         В уроке должна быть базовая информация:
#         название, ссылка на видео, длительность просмотра (в секундах).
#     """
#     lesson_name = models.CharField(max_length=64, verbose_name='Название урока')
#     lesson_link = models.URLField(null=True, blank=True, verbose_name='URL на урок')
#     lesson_time = models.PositiveIntegerField(verbose_name='Продолжительность')
#
#     def __str__(self):
#         return '{}'.format(self.lesson_name)
#
#     class Meta:
#         verbose_name = 'Урок'
#         verbose_name_plural = 'Уроки'
