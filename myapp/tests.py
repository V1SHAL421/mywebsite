from django.forms import ValidationError
from django.test import TestCase

from myapp.models import User

class UserModelTestCase(TestCase):
    def test_valid_user(self):
        pass
        user = User.objects.create_user(
            "evasmith54"
            first_name = "Eva"
            surname = "Smith"
            bio = "Hey guys I am a friendly person :)"
            email = evasmith@example.com
            new_password = "Password123"
            password_confirmation = "Password123"
        )
        try:
            user.full_clean()
        except ValidationError:
            self.fail('Test user should be valid')

class UnitTestCase(TestCase):
    def test(self):
        pass
