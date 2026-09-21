from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # مساراتك الحالية مثل login و logout ...
    path('profile/', views.profile_view, name='profile'),
    path('orders/<int:order_id>/', views.order_detail_view, name='order_detail'),
]