"""Tests of the login view"""
from django.contrib.auth.hashers import check_password
from django.test import TestCase
from django.urls import reverse
from myapp.forms import LoginForm
from myapp.models import User

class LoginViewTestCase(TestCase):
    """Tests of the login view"""

    def setUp(self):
        self.url = reverse('login')

    def test_login_url(self):
        self.assertEqual(reverse('login'),'/login/')

    def test_get_login(self):
        # self.client # simulates response problematically
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LoginForm))
        self.assertFalse(form.is_bound)