from django.urls import path
from application import views


urlpatterns = [
    path('prod/', views.ProductViewSet.as_view({'get': 'list'}),),
    path('lesson/', views.LessonViewSet.as_view({'get': 'list'})),
]
