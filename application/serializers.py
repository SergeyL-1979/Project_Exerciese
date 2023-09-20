from rest_framework import serializers

from application.models import Product, Lesson
from users.serializers import UserSerializer


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ["lesson_name", "lesson_link", "lesson_time", ]


class ProductSerializer(serializers.ModelSerializer):
    author_product = UserSerializer()
    lesson_product = LessonSerializer(many=True)

    class Meta:
        model = Product
        fields = ["name_product", "author_product", "lesson_product", ]








