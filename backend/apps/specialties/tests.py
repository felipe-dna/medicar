"""
Contains the Specialties app tests.

https://docs.djangoproject.com/en/3.1/topics/testing/overview/
"""

from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Speciality


class SpecialityModelTestCase(TestCase):
    """Define the speciality model tests."""

    def test_create_two_specialties_with_the_same_name(self) -> None:
        """Try to create two specialties using the same name."""
        speciality_name = 'pediatrics'
        expected_error_message = 'Speciality with this Speciality name already exists.'

        Speciality.objects.create(name=speciality_name)

        with self.assertRaisesMessage(ValidationError, expected_error_message):
            Speciality.objects.create(name=speciality_name)
