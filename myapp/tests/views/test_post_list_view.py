"""Tests of the post list view"""
from django.test import TestCase
from django.urls import reverse

from myapp.models import Post
from ..helpers import LogInTester
from django.contrib.auth import get_user_model 

class PostListViewTestCase(TestCase, LogInTester):
    """Tests of the post list view"""

    def setUp(self):
        self.url = reverse('post_list')
        custom_user = get_user_model()
        self.user = custom_user.objects.create_user('@johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            bio='Hello, I am John',
            password='Password123',
            is_active=True)

    def test_post_list_url(self):
        self.assertEqual(self.url,'/posts/')

    def test_get_post_list_redirects_when_not_logged_in(self):
        response = self.client.get(self.url)
        # self.assertEqual(self.url,'/log_in/?next=/posts/')
        self.assertRedirects(response, '/log_in/?next=/posts/')

    def test_get_post_list_without_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'post_list.html')

    def test_get_post_list_with_login(self):
        self.client.login(username=self.user.username, password="Password123")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')

    def test_post_list_with_no_posts(self):
        Post.objects.all().delete()
        self.client.login(username=self.user.username, password="Password123")
        response = self.client.get(self.url)
        self.assertContains(response, "You have not created a post yet.")