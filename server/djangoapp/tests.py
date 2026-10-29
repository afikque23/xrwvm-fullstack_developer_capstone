from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
import json


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            first_name='Test',
            last_name='User',
            email='test@example.com'
        )

    def test_login_valid(self):
        response = self.client.post(
            '/djangoapp/login/',
            json.dumps({'userName': 'testuser', 'password': 'testpass123'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data.get('status'), 'Authenticated')

    def test_login_invalid(self):
        response = self.client.post(
            '/djangoapp/login/',
            json.dumps({'userName': 'testuser', 'password': 'wrongpass'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertNotEqual(data.get('status'), 'Authenticated')

    def test_registration(self):
        response = self.client.post(
            '/djangoapp/register/',
            json.dumps({
                'userName': 'newuser',
                'password': 'newpass123',
                'firstName': 'New',
                'lastName': 'User',
                'email': 'new@example.com'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data.get('status'), 'Authenticated')
