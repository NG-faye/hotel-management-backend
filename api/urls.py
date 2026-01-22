from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, RegisterView

router = DefaultRouter()
router.register(r'hotels', HotelViewSet, basename='hotel')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]