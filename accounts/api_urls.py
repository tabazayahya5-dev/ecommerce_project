from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import RegisterView, UserProfileView, AddressViewSet

router = DefaultRouter()
router.register(r'addresses', AddressViewSet, basename='address')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    
    path('', include(router.urls)),
]