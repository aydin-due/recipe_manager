from django.contrib.auth.password_validation import validate_password
from django.test import TestCase
import os

class RecipeManagerConfigTest(TestCase):
    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        # self.assertNotEqual(SECRET_KEY, 'abc123')
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'weak secret key {e.messages}'
            self.fail(msg)