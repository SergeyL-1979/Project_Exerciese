from rest_framework import serializers

from application.models import Product, ProductAccess
from lesson.models import Lesson, LessonInfo
from users.serializers import UserSerializer


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonInfo
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    author_product = UserSerializer()
    lesson_product = LessonSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductAccessSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductAccess
        fields = '__all__'







