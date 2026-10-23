from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from drf_spectacular.views import (SpectacularAPIView,SpectacularSwaggerView,SpectacularRedocView,)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/accounts/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/accounts/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/products/', include('products.api_urls')), 
    path('api/v1/accounts/', include('accounts.api_urls')),
    path('api/v1/cart/', include('cart.api_urls')),
    path('api/v1/orders/', include('orders.api_urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('products.urls', namespace='products')),
    path('orders/', include('orders.urls', namespace='orders')),
]