import datetime

from django.db import models

from users.models import User


# В этом задании у нас есть три бизнес-задачи на хранение:

# 3. Урок могут просматривать множество пользователей.
#    Необходимо для каждого фиксировать время просмотра и
#    фиксировать статус “Просмотрено”/”Не просмотрено”.
#    Статус “Просмотрено” проставляется, если пользователь просмотрел 80% ролика.

class Product(models.Model):
    """
    1. Создать сущность продукта. У продукта должен быть владелец.
        Необходимо добавить сущность для сохранения доступов к продукту для пользователя."""
    name_product = models.CharField(max_length=100, verbose_name='Название')
    author_product = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name='Автор')
    lesson_product = models.ManyToManyField('Lesson', blank=True, verbose_name='TT')

    def __str__(self):
        return '{}'.format(self.name_product)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Lesson(models.Model):
    """
    2. Создать сущность урока. Урок может находиться в нескольких продуктах одновременно.
        В уроке должна быть базовая информация:
        название, ссылка на видео, длительность просмотра (в секундах).
    """
    lesson_name = models.CharField(max_length=64, verbose_name='Название урока')
    lesson_link = models.URLField(null=True, blank=True, verbose_name='URL на урок')
    lesson_time = models.TimeField(verbose_name='Продолжительность')
    # lesson_time = models.PositiveIntegerField(max_length=10000, verbose_name='Продолжительность')
    # lesson_prod = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True,)

    def __str__(self):
        return '{}'.format(self.lesson_name)


