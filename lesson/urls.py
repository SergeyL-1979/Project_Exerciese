from django.urls import path
from lesson import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'prod', views.ProductViewSet)
router.register(r'prodaccess', views.ProductAccessViewSet)
router.register(r'lesson', views.LessonViewSet)
router.register(r'lessoninfo', views.LessonInfoViewSet)


urlpatterns = [
    # path('prod/', views.ProductViewSet.as_view({'get': 'list'}),),
    # path('lesson/', views.LessonViewSet.as_view({'get': 'list'})),
]

urlpatterns += router.urls
