from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'city', 'paid', 'status', 'created_at']
    list_filter = ['paid', 'status', 'created_at']
    inlines = [OrderItemInline]