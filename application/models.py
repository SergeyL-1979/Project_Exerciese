from django.db import models


# В этом задании у нас есть три бизнес-задачи на хранение:
# 1. Создать сущность продукта. У продукта должен быть владелец.
#    Необходимо добавить сущность для сохранения доступов к продукту для пользователя.

# 2. Создать сущность урока. Урок может находиться в нескольких продуктах одновременно.
#    В уроке должна быть базовая информация:
#    название, ссылка на видео, длительность просмотра (в секундах).

# 3. Урок могут просматривать множество пользователей.
#    Необходимо для каждого фиксировать время просмотра и
#    фиксировать статус “Просмотрено”/”Не просмотрено”.
#    Статус “Просмотрено” проставляется, если пользователь просмотрел 80% ролика.
