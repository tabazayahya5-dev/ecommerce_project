from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Product, Category
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()  

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.product = Product.objects.create(
            name="Test Laptop",
            description="A high-performance testing laptop",
            price=999.99,
            stock=10,
            category=self.category
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Laptop")
        self.assertEqual(self.product.price, 999.99)
        self.assertEqual(self.product.stock, 10)
        self.assertEqual(self.product.category, self.category)

class ProductAPITest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Test Phone",
            description="Testing Phone",
            price=500.00,
            stock=5,
            category=self.category
        )
        self.list_url = reverse('product-list')  

    def test_get_product_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_create_product(self):
        user = User.objects.create_user(username='testuser', password='password123')
        self.client.force_authenticate(user=user)  

        data = {
            "name": "New Gaming Laptop",
            "slug": "new-gaming-laptop",  
            "description": "Powerful gaming machine",
            "price": 1499.99,
            "stock": 3,
            "category_id": self.category.id  
        }
        
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_update_product(self):
        user = User.objects.create_user(username='testuser2', password='password123')
        self.client.force_authenticate(user=user)

        updated_data = {
            "name": "Updated Laptop Name",
            "slug": "updated-laptop-name",
            "description": "Updated description",
            "price": 1999.99,
            "stock": 10,
            "category_id": self.category.id
        }

        detail_url = reverse('product-detail', kwargs={'pk': self.product.id})

        response = self.client.put(detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Updated Laptop Name")
        self.assertEqual(float(self.product.price), 1999.99)

    def test_delete_product(self):
        user = User.objects.create_user(username='testuser3', password='password123')
        self.client.force_authenticate(user=user)

        detail_url = reverse('product-detail', kwargs={'pk': self.product.id})

        response = self.client.delete(detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        self.assertEqual(Product.objects.count(), 0)
        