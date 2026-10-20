from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/v1/products/', include('products.api_urls')), 

    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('products.urls', namespace='products')),
    path('orders/', include('orders.urls', namespace='orders')),
]