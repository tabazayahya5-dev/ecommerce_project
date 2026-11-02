from django.test import TestCase
from django.contrib.auth import get_user_model
from products.models import Category, Product
from cart.models import Cart, CartItem
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

User = get_user_model()

class CartModelTest(TestCase):
    def setUp(self):
        self.user =User.objects.create_user(username='cartuser' , password='password')
        self.cart = Cart.objects.create(user=self.user)
        self.category =Category.objects.create(name='Electronics', slug='electronics')

        self.product = Product.objects.create(
            name='Test Smartphone',
            slug='test-smartphone',
            price=500.00,
            stock=10,
            category=self.category
        )

    def test_cart_string_representation(self):
        self.assertEqual(str(self.cart), "Cart (cartuser)")

    def test_cart_item_creation_and_cost(self):
        cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=2
        )

        self.assertEqual(cart_item.get_cost(), 1000.00)

        self.assertEqual(self.cart.get_total_price(), 1000.00)

class CartAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='apiuser', password='password123')
        self.cart = Cart.objects.create(user=self.user)
        self.category = Category.objects.create(name='Electronics', slug='electronics')
        self.product = Product.objects.create(
            name='Laptop',
            slug='laptop',
            price=1200.00,
            stock=5,
            category=self.category
        )
        self.cart_url = reverse('cart-item-list')

    def test_add_item_to_cart(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "product_id": self.product.id,
            "quantity": 2
        }
        response = self.client.post(self.cart_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CartItem.objects.count(), 1)
        self.assertEqual(CartItem.objects.first().quantity, 2)

    def test_get_cart_items(self):
        CartItem.objects.create(cart=self.cart, product=self.product, quantity=3)
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.cart_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_update_cart_item_quantity(self):
        cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)
        
        item_url = reverse('cart-item-detail', kwargs={'pk': cart_item.id})
        
        self.client.force_authenticate(user=self.user)
        data = {
            "product_id": self.product.id,
            "quantity": 5
        }
        response = self.client.put(item_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cart_item.refresh_from_db()
        self.assertEqual(cart_item.quantity, 5)

    def test_delete_cart_item(self):
        cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=1)
        item_url = reverse('cart-item-detail', kwargs={'pk': cart_item.id})
        self.client.force_authenticate(user=self.user)
        
        response = self.client.delete(item_url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CartItem.objects.count(), 0)

    def test_unauthenticated_user_cannot_access_cart(self):
        self.client.logout()
        
        response = self.client.get(self.cart_url)
        
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_user_cannot_access_other_user_cart_items(self):
        cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=1)
        
        other_user = User.objects.create_user(username='otheruser', password='password123')
        
        item_url = reverse('cart-item-detail', kwargs={'pk': cart_item.id})
        self.client.force_authenticate(user=other_user)
        response = self.client.get(item_url)
        
        self.assertIn(response.status_code, [status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN])


