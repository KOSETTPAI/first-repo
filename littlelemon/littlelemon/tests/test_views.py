from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class MenuViewTest(TestCase):

    def setUp(self):
        self.item1 = Menu.objects.create(title="Pizza", price=12.99, inventory=50)
        self.item2 = Menu.objects.create(title="Burger", price=5.99, inventory=30)
        self.item3 = Menu.objects.create(title="Pasta", price=8.99, inventory=20)

        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()
        self.client.login(username='testuser', password='password')

    def test_getall(self):
        url = reverse('menu-list')

        response = self.client.get(url)
        

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serialized_data = response.data
        
        expected_data = [
            {'id': self.item1.id, 'title': 'Pizza', 'price': '12.99', 'inventory': 50},
            {'id': self.item2.id, 'title': 'Burger', 'price': '5.99', 'inventory': 30},
            {'id': self.item3.id, 'title': 'Pasta', 'price': '8.99', 'inventory': 20},
        ]
        
        self.assertEqual(serialized_data, expected_data)