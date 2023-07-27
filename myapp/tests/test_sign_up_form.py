from django import forms
from django.forms import EmailField
from django.urls import reverse
from myapp.forms import SignUpForm
from django.test import TestCase
from myapp.models import User
from django.contrib.auth.hashers import check_password

class SignUpFormTestCase(TestCase):
    """Unit tests for the sign up form"""

    def setUp(self):
        self.form_input = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'username': '@janedoe',
            'email': 'janedoe@example.org',
            'bio': 'My bio',
            'new_password': 'Password123',
            'password_confirmation': 'Password123'
        }


    def test_valid_sign_up_form(self):
        form = SignUpForm(data=self.form_input)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_form_has_necessary_fields(self):
        form = SignUpForm()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('username', form.fields)
        self.assertIn('email', form.fields)
        email_field = form.fields['email']
        self.assertTrue(isinstance(email_field, EmailField))
        self.assertIn('bio', form.fields)
        self.assertIn('new_password', form.fields)
        new_password_widget = form.fields['new_password'].widget
        self.assertTrue(isinstance(new_password_widget, forms.PasswordInput))
        self.assertIn('password_confirmation', form.fields)
        password_confirmation_widget = form.fields['password_confirmation'].widget
        self.assertTrue(isinstance(password_confirmation_widget, forms.PasswordInput))

    def test_form_users_model_validation(self):
        self.form_input['username'] = 'badusername'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    # New password has correct format
    def test_password_must_contain_uppercase_character(self):
        self.form_input['new_password'] = 'badpassword123'
        self.form_input['password_confirmation'] = 'badpassword123'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_must_contain_lowercase_character(self):
        self.form_input['new_password'] = 'BADPASSWORD123'
        self.form_input['password_confirmation'] = 'BADPASSWORD123'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())


    def test_password_must_contain_number(self):
        self.form_input['new_password'] = 'badPASSWORD'
        self.form_input['password_confirmation'] = 'badPASSWORD123'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_new_password_and_password_confirmation_are_identical(self):
        self.form_input['password_confirmation'] = 'WrongPassword123'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_must_save_correctly(self):
        form = SignUpForm(data=self.form_input)
        before_count = User.objects.count()
        form.save()
        after_count = User.objects.count()
        self.assertEqual(after_count, before_count+1)
        user = User.objects.get(username='@janedoe')
        self.assertEqual(user.first_name, 'Jane')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.username, '@janedoe')
        self.assertEqual(user.email, 'janedoe@example.org')
        self.assertEqual(user.bio, 'My bio')
        is_password_correct = check_password('Password123', user.password) # compares hash of password
        self.assertTrue(is_password_correct)

    # New password and password confirmation are identical