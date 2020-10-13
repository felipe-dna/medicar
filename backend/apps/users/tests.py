"""
Contains the users app tests.

https://docs.djangoproject.com/en/3.1/topics/testing/overview/
"""

from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import User


class UserModelTestCase(TestCase):
    """Define the user model tests."""

    def test_create_two_users_with_the_same_email(self) -> None:
        """Try to create two users using the same email."""
        email_example = 'test@gmail.com'
        expected_error_message = 'User with this Email already exists.'

        User.objects.create_user(
            email=email_example,
            password='some-secure-password',
        )

        with self.assertRaisesMessage(ValidationError, expected_error_message):
            User.objects.create(
                email=email_example,
                password='another-secure-password'
            )

    def test_create_user_passing_wrong_email_format(self) -> None:
        """Try to create a user passing a invalid email format."""
        expected_error_message = 'Enter a valid email address'

        with self.assertRaisesMessage(ValidationError, expected_error_message):
            User.objects.create(
                email='a-invalid-email-format',
                password='another-secure-password',
            )
