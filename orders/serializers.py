from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'price', 'quantity', 'subtotal']

    def get_subtotal(self, obj):
        return obj.get_cost()


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id', 'user', 'first_name', 'last_name', 'email', 
            'address', 'city', 'paid', 'status', 'created_at', 
            'updated_at', 'items', 'total_cost'
        ]
        read_only_fields = ['id', 'user', 'paid', 'status', 'created_at', 'updated_at']

    def get_total_cost(self, obj):
        return obj.get_total_cost()