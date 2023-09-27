from rest_framework import serializers

from application.models import Product, ProductAccess
from lesson.models import Lesson, LessonInfo
from users.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Product
        fields = ["title", "user", ]


class ProductAccessSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductAccess
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ["title", "url_link", "video_duration", "products", ]


class LessonInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonInfo
        fields = ["lesson", "user", "status", "video_view", ]


