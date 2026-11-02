from django.test import TestCase
from django.contrib.auth import get_user_model
from products.models import Category, Product
from orders.models import Order, OrderItem
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from cart.models import Cart, CartItem

User = get_user_model()

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='orderuser', password='password123')
        self.category = Category.objects.create(name='Electronics', slug='electronics')
        self.product = Product.objects.create(
            name='Smartphone',
            slug='smartphone',
            price=500.00,
            stock=10,
            category=self.category
        )
        
        self.order = Order.objects.create(
            user=self.user,
            first_name='Yahya',
            last_name='Tabaza',
            email='yahya@example.com',
            address='Abu Areef Street',
            city='Deir Al-Balah'
        )

    def test_order_string_representation(self):
        expected_str = f"Order {self.order.id} - {self.user.username}"
        self.assertEqual(str(self.order), expected_str)

    def test_order_item_cost_and_total(self):
        order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            price=self.product.price,
            quantity=2
        )
        
        self.assertEqual(order_item.get_cost(), 1000.00)
        self.assertEqual(self.order.get_total_cost(), 1000.00)

class OrderAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='apiorderuser', password='password123')
        self.client.force_authenticate(user=self.user)
        
        self.cart = Cart.objects.create(user=self.user)
        
        self.category = Category.objects.create(name='Electronics', slug='electronics')
        self.product = Product.objects.create(
            name='Headphones',
            slug='headphones',
            price=150.00,
            stock=10,
            category=self.category
        )
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)
        
        self.order_url = reverse('order-list-create')

    def test_create_order_from_cart(self):
        data = {
            "first_name": "Yahya",
            "last_name": "Tabaza",
            "email": "yahya@example.com",
            "address": "Abu Areef Street",
            "city": "Deir Al-Balah"
        }
        
        response = self.client.post(self.order_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(Order.objects.count(), 1)
        created_order = Order.objects.first()
        self.assertEqual(created_order.user, self.user)
        self.assertEqual(created_order.city, 'Deir Al-Balah')

    def test_get_user_orders(self):
        Order.objects.create(
            user=self.user,
            first_name='Yahya',
            last_name='Tabaza',
            email='yahya@example.com',
            address='Abu Areef Street',
            city='Deir Al-Balah'
        )
        
        response = self.client.get(self.order_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        results = response.data['results'] if 'results' in response.data else response.data
        self.assertEqual(len(results), 1)

    def test_cart_is_cleared_after_order_creation(self):
        self.assertEqual(CartItem.objects.filter(cart=self.cart).count(), 1)
        
        data = {
            "first_name": "Yahya",
            "last_name": "Tabaza",
            "email": "yahya@example.com",
            "address": "Abu Areef Street",
            "city": "Deir Al-Balah"
        }
        response = self.client.post(self.order_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CartItem.objects.filter(cart=self.cart).count(), 0)