"""Tests of the log out view"""
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.test import TestCase
from django.urls import reverse
from myapp.forms import LogInForm
from myapp.models import User
from .helpers import LogInTester
from django.contrib.auth import get_user_model 

class LogInViewTestCase(TestCase, LogInTester):
    """Tests of the log out view"""

    def setUp(self):
        self.url = reverse('log_out')
        custom_user = get_user_model()
        self.user = custom_user.objects.create_user('@johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            bio='Hello, I am John',
            password='Password123',
            is_active=True)

    def test_log_out_url(self):
        self.assertEqual(self.url,'/log_out/')

    def test_get_log_out(self):
        self.client.login(username='@johndoe', password='Password123')
        self.assertTrue(self._is_logged_in())
        response = self.client.get(self.url, follow=True)
        response_url = reverse('home')
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertFalse(self._is_logged_in())
