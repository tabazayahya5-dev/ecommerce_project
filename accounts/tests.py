from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from accounts.models import Address  

User = get_user_model()

class AccountsAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123',
            first_name='Yahya',
            last_name='Tabaza',
            phone_number='123456789'
        )
        
        self.register_url = reverse('register')      
        self.profile_url = reverse('profile')   
        self.address_url = reverse('address-list')   

    def test_user_registration(self):
        data = {
            "username": "newuser",
            "email": "new@example.com",
            "password": "securepassword123",
            "first_name": "Ahmad",
            "last_name": "Ali",
            "phone_number": "987654321"
        }
        response = self.client.post(self.register_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.filter(username='newuser').exists(), True)

    def test_get_user_profile_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.profile_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['email'], self.user.email)

    def test_get_user_profile_unauthenticated(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_and_list_address(self):
        self.client.force_authenticate(user=self.user)
        
        address_data = {
            "city": "Deir Al-Balah",
            "street": "Abu Areef Street",
            "building_number": "10",
            "is_default": True
        }
        
        response = self.client.post(self.address_url, address_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(Address.objects.first().city, "Deir Al-Balah")
        
        get_response = self.client.get(self.address_url)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        
        results = get_response.data['results'] if 'results' in get_response.data else get_response.data
        self.assertEqual(len(results), 1)