from django.db import models

from users.models import User


# В этом задании у нас есть три бизнес-задачи на хранение:

# 3. Урок могут просматривать множество пользователей.
#    Необходимо для каждого фиксировать время просмотра и
#    фиксировать статус “Просмотрено”/”Не просмотрено”.
#    Статус “Просмотрено” проставляется, если пользователь просмотрел 80% ролика.

class Product(models):
    """
    1. Создать сущность продукта. У продукта должен быть владелец.
        Необходимо добавить сущность для сохранения доступов к продукту для пользователя."""
    name_product = models.CharField(max_length=100, verbose_name='Название')
    author_product = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Lesson(models):
    """
    2. Создать сущность урока. Урок может находиться в нескольких продуктах одновременно.
        В уроке должна быть базовая информация:
        название, ссылка на видео, длительность просмотра (в секундах).
    """
    lesson_name = models.CharField(max_length=64, unique=True, verbose_name='Название урока')
    lesson_link = models.URLField(verbose_name='Ссылка на урок')
    lesson_time = models.TimeField(verbose_name='Продолжительность')
    lesson_prod = models.ManyToManyField(Product, blank=True, through='Product')
