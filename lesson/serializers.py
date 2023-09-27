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


class LessonInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonInfo
        fields = ["lesson", "user", "status", "video_view", ]


class LessonSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)
    status = serializers.CharField()
    view_time = serializers.IntegerField()

    # ===== Как можно делать запрос к БД но  это не правильно. Их получается слишком много =======
    # view_info = serializers.SerializerMethodField()
    # def get_view_info(self, obj):
    #     view_info = LessonInfo.objects.get(user=self.context['user_id'], lesson_id=obj.id)
    #     return LessonInfoSerializer(view_info).data
    # =============================================================================================

    class Meta:
        model = Lesson
        # fields = ["title", "status", "view_time", "video_duration", "url_link", "products", ]
        fields = ["title", "status", "view_time", ]





