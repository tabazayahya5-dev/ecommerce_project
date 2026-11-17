from django.urls import path
from .api_views import (
    OrderListCreateView,
    OrderDetailView,
    CreateCheckoutSessionView,
    StripeWebhookView,
)

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list-create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('<int:order_id>/pay/', CreateCheckoutSessionView.as_view(), name='order-pay'),
    path('webhook/', StripeWebhookView.as_view(), name='stripe-webhook'),
]