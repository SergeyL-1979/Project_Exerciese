from django.http import Http404
from rest_framework import permissions

from application.models import Product, Lesson, UserLesson, UserProduct


class LessonPermissions(permissions.BasePermission):

    # def has_permission(self, request, view):
    #     # return bool(request.user and request.user.is_staff)
    #
    #     if not request.user.is_authenticated:
    #         return False
    #     if request.method in permissions.SAFE_METHODS:
    #         return UserProduct.objects.filter(user=request.user, ).exists()

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:
            # return UserLesson.objects.filter(user=request.user, lesson=obj).exists()
            # return UserProduct.objects.all()
            return UserProduct.objects.filter(user=request.user, product=obj.product.all()).exists()
