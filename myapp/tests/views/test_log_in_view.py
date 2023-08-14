"""Tests of the log in view"""
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.test import TestCase
from django.urls import reverse
from myapp.forms import LogInForm
from myapp.models import User
from ..helpers import LogInTester
from django.contrib.auth import get_user_model 

class LogInViewTestCase(TestCase, LogInTester):
    """Tests of the log in view"""


    def setUp(self):
        self.url = reverse('log_in')
        custom_user = get_user_model()
        self.user = custom_user.objects.create_user('@johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            bio='Hello, I am John',
            password='Password123',
            is_active=True)

    def test_log_in_url(self):
        self.assertEqual(reverse('log_in'),'/log_in/')

    def test_get_log_in(self):
        # self.client # simulates response problematically
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(form.is_bound)
        messages_list = list(response.context['messages'])
        self.assertEqual(len(messages_list), 0)

    def test_unsuccessful_log_in(self):
        form_input = {'username': '@johndoe', 'password': 'WrongPassword123'}
        response = self.client.post(self.url, form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(self._is_logged_in())
        messages_list = list(response.context['messages'])
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].level, messages.ERROR)


    def test_successful_log_in(self):
        form_input = {'username': '@johndoe', 'password': 'Password123'}
        response = self.client.post(self.url, form_input)
        self.assertTrue(self._is_logged_in())

    def test_successful_log_in_redirect(self):
        form_input = {'username': '@johndoe', 'password': 'Password123'}
        response = self.client.post(self.url, form_input, follow=True)
        self.assertRedirects(response, reverse('feed'), status_code=302, target_status_code=200)
        self.assertTrue(self._is_logged_in())
        messages_list = list(response.context['messages'])
        self.assertEqual(len(messages_list), 0)

    def test_valid_log_in_by_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        form_input = {'username': '@johndoe', 'password': 'Password123'}
        response = self.client.post(self.url, form_input)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(self._is_logged_in())
        messages_list = list(response.context['messages'])
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].level, messages.ERROR)



