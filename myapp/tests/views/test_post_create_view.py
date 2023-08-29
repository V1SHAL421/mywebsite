"""Tests of the post create view"""
from django.test import TestCase
from django.urls import reverse
from ..helpers import LogInTester
from django.contrib.auth import get_user_model 

class PostCreateViewTestCase(TestCase, LogInTester):
    """Tests of the post create view"""

    def setUp(self):
        self.url = reverse('post_create')
        custom_user = get_user_model()
        self.user = custom_user.objects.create_user('@johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            bio='Hello, I am John',
            password='Password123',
            is_active=True)
        
    def test_post_create_url(self):
        self.assertEqual(self.url,'/post/create/')

    def test_get_post_list_redirects_when_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, '/log_in/?next=/post/create/')

    def test_get_post_create_without_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'post_create.html')
    
    def test_get_post_list_with_login(self):
        self.client.login(username=self.user.username, password="Password123")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_create.html')