"""Unit tests of the post form."""

from django.contrib.auth.hashers import check_password
from django.test import TestCase
from django.urls import reverse
from django import forms
from myapp.forms import LogInForm

class PostFormTestCase(TestCase):
    """Unit tests of the post form."""

    # def setUp(self):
    #     self.form_input = {'username': '@janedoe', 'password': 'Password123'}