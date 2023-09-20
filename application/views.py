from rest_framework import viewsets
from rest_framework import generics

from application.models import Product, Lesson
from application.serializers import ProductSerializer, LessonSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
