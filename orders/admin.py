from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0
    readonly_fields = ['price'] 


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'user', 
        'first_name', 
        'last_name', 
        'email', 
        'status', 
        'created_at', 
        'get_total_cost'
    ]
    list_filter = ['status', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'address']
    list_editable = ['status']  
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price', 'quantity']