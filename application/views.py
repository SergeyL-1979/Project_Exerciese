from rest_framework import viewsets, permissions
from rest_framework import generics

from application.models import Product, Lesson
from application.permissions import LessonPermissions
from application.serializers import ProductSerializer, LessonSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, LessonPermissions]
