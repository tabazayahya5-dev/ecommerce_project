from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.permissions import AllowAny
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@method_decorator(cache_page(60 * 15), name='dispatch') 
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends =[DjangoFilterBackend , SearchFilter ,OrderingFilter]
    filterset_fields = ['category', 'is_active']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']

    def perform_create(self, serializer):
        serializer.save()
        cache.clear()  
    
    def perform_update(self, serializer):
        serializer.save()
        cache.clear()  

    def perform_destroy(self, instance):
        instance.delete()
        cache.clear() 
