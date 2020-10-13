"""
Contains the schedules app tests.

https://docs.djangoproject.com/en/3.1/topics/testing/overview/
"""

from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import DoctorScheduleTime, DoctorSchedule


class DoctorScheduleTimeModelTestCase(TestCase):
    """Define the doctor schedule time model tests."""

    def test_create_a_schedule_time_passing_wrong_time_format(self) -> None:
        """"""
        invalid_time_format = 'a invalid time format'
        expected_message = f"{invalid_time_format}” value has an invalid " \
                           f"format. It must be in HH:MM[:ss[.uuuuuu]] format."

        with self.assertRaisesMessage(ValidationError, str(expected_message)):
            DoctorScheduleTime.objects.create(time=invalid_time_format)

