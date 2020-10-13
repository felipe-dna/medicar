"""
Contains the doctors app tests.

https://docs.djangoproject.com/en/3.1/topics/testing/overview/
"""

from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Doctor
from ..specialties.models import Speciality


class DoctorModelTestCase(TestCase):
    """Define the doctor model tests."""

    def setUp(self) -> None:
        """"""

        self.speciality = Speciality.objects.create(name="pediatrics")

    def test_try_to_create_a_doctor_passing_a_invalid_email_format(self) -> None:
        """"""

        expected_message = "Enter a valid email address."

        with self.assertRaisesMessage(ValidationError, expected_message):
            Doctor.objects.create(
                email="invalid-email-format",
                name='John Doe',
                crm='4444',
                phone='12345678901',
                speciality=self.speciality
            )

    def test_try_to_create_two_doctors_with_the_same_crm(self) -> None:
        """"""

        expected_message = "Doctor with this CRM already exists."

        Doctor.objects.create(
            email="jhon@doe.com",
            name='John Doe',
            crm='4444',
            phone='12345678901',
            speciality=self.speciality
        )

        with self.assertRaisesMessage(ValidationError, expected_message):
            Doctor.objects.create(
                email="joan@doe.com",
                name='Joan Doe',
                crm='4444',
                phone='12345678901',
                speciality=self.speciality
            )

    def test_try_to_create_a_doctor_passing_a_crm_with_length_grater_than_4(self) -> None:
        """"""

        expected_message = "Ensure this value has at most 4 characters (it has 5)."
        with self.assertRaisesMessage(ValidationError, expected_message):
            Doctor.objects.create(
                email="joan@doe.com",
                name='Joan Doe',
                crm='44444',
                phone='12345678901',
                speciality=self.speciality
            )

    def test_try_to_create_two_doctors_with_the_same_email(self) -> None:
        """"""

        expected_message = "Doctor with this Email already exists."

        Doctor.objects.create(
            email="jhon@doe.com",
            name='John Doe',
            crm='4444',
            phone='12345678901',
            speciality=self.speciality
        )

        with self.assertRaisesMessage(ValidationError, expected_message):
            Doctor.objects.create(
                email="jhon@doe.com",
                name='Joan Doe',
                crm='5555',
                phone='12345678901',
                speciality=self.speciality
            )

    def test_try_to_create_a_doctor_passing_a_alphabetic_crm(self) -> None:
        """"""

        expected_message = "The CRM must be a numeric value."

        with self.assertRaisesMessage(ValidationError, expected_message):
            Doctor.objects.create(
                email="jhon@doe.com",
                name='Joan Doe',
                crm='ACRM',
                phone='12345678901',
                speciality=self.speciality
            )

    def test_try_to_create_a_doctor_passing_a_phone_number_with_less_than_ten_characters(self) -> None:
        """"""

        expected_message = "A phone number must have at least 8 characters."

        with self.assertRaisesMessage(ValidationError, expected_message):
            Doctor.objects.create(
                email="jhon@doe.com",
                name='Joan Doe',
                crm='4444',
                phone='123456789',
                speciality=self.speciality
            )
