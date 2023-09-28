from django.db.models import FilteredRelation, Q, F
from rest_framework import viewsets, permissions, exceptions
from rest_framework import generics

from application.models import Product, ProductAccess

from lesson.models import Lesson, LessonInfo
from lesson.serializers import ProductSerializer, LessonSerializer, ProductAccessSerializer, LessonInfoSerializer


def get_accesses(user):
    return ProductAccess.objects.filter(user=user, is_valid=True)


class ProductViewSet(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        accesses = get_accesses(self.request.user)

        if not (product_id in accesses.values_list('product_id', flat=True)):
            raise exceptions.NotFound

        qs = Lesson.objects.filter(
            products=product_id
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=self.request.user)
            )
        ).annotate(
            status=F('view_info__status'),
            view_time=F('view_info__video_view'),
            last_view_datetime=F('view_info__last_view_datetime')
        )

        return qs


# class ProductAccessViewSet(viewsets.ModelViewSet):
#     queryset = ProductAccess.objects.all()
#     serializer_class = ProductAccessSerializer


class LessonViewSet(viewsets.ModelViewSet):
    # queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        # accesses = ProductAccess.objects.filter(user=self.request.user, is_valid=True)
        accesses = get_accesses(self.request.user)

        qs = Lesson.objects.filter(
            products__in=accesses.values("product_id")
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=self.request.user)
            )
        ).annotate(
            status=F('view_info__status'),
            view_time=F('view_info__video_view')
        )

        return qs


# class LessonInfoViewSet(viewsets.ModelViewSet):
#     queryset = LessonInfo.objects.all()
#     serializer_class = LessonInfoSerializer
