from django.urls import path
from lesson import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'prod', views.ProductViewSet, basename='product')
router.register(r'prodaccess', views.ProductAccessViewSet, basename='product_access')
router.register(r'lesson', views.LessonViewSet, basename='lesson')
router.register(r'lessoninfo', views.LessonInfoViewSet, basename='lesson_info')


urlpatterns = [
    # path('prod/', views.ProductViewSet.as_view({'get': 'list'}),),
    # path('lesson/', views.LessonViewSet.as_view({'get': 'list'})),
]

urlpatterns += router.urls
