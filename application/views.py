from django.db.models import Count, OuterRef, Sum, F
from rest_framework import viewsets, permissions, exceptions
from rest_framework import generics

from application.models import Product, ProductAccess
from application.serializers import ProductStatisticSerializer

from lesson.models import LessonInfo, LessonStatus
from lesson.serializers import ProductSerializer, LessonSerializer, ProductAccessSerializer, LessonInfoSerializer
from users.models import User


class ProductStatisticViewSet(viewsets.ModelViewSet):
    serializer_class = ProductStatisticSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        total_users_count = User.objects.filter(is_active=True).count()

        qs = Product.objects.all().annotate(
            lesson_count_view=Count(
                LessonInfo.objects.filter(
                    lesson__products=OuterRef('id'),
                    status=LessonStatus.VIEWED
                ).values('id')
            ),
            total_view=Sum(
                LessonInfo.objects.filter(
                    lesson__products=OuterRef('id'),
                ).values('video_view')
            ),
            total_users_product=Count(
                ProductAccess.objects.filter(product_id=OuterRef('id')).values('id')
            ),
            percent_products=F('total_users_product') / float(total_users_count) * 100
        )

        return qs


