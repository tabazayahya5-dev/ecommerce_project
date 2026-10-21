from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CartDetailView, CartItemViewSet

router = DefaultRouter()
router.register(r'items', CartItemViewSet, basename='cart-item')

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart-detail'),
    path('', include(router.urls)),
]