from django.urls import path, include
from lesson import views
from rest_framework import routers

# router = routers.DefaultRouter()
router = routers.SimpleRouter()
router.register('my-lesson', views.LessonViewSet, 'my-lesson')

# router.register('prod', views.ProductViewSet, basename='product')
# router.register('prod-access', views.ProductAccessViewSet, basename='product_access')
# router.register('lesson', views.LessonViewSet, basename='lesson')
# router.register('lesson-info', views.LessonInfoViewSet, basename='lesson_info')


urlpatterns = [
    path('', include(router.urls)),
    path('by-product/<int:product_id>/lessons/', views.ProductViewSet.as_view({'get': 'list'}),),
    # path('lesson/', views.LessonViewSet.as_view({'get': 'list'})),
]

# urlpatterns += router.urls
