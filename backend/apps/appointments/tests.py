"""
Contains the appointments app tests.

https://docs.djangoproject.com/en/3.1/topics/testing/overview/
"""

from django.core.exceptions import ValidationError
from django.test import TestCase

from ..doctors.models import Doctor
from ..schedules.models import DoctorScheduleTime, DoctorSchedule
from ..specialties.models import Speciality
from .models import Appointment
from ..users.models import User


class AppointmentModelTestCase(TestCase):
    """Define the doctor model tests."""

    def setUp(self) -> None:
        """Create the necessary resources that is used by some tests."""
        speciality = Speciality.objects.create(name="pediatrics")
        self.doctor = Doctor.objects.create(
            name='John Doe',
            crm='1111',
            email='jhon@doe.com',
            phone='99999999999',
            speciality=speciality
        )
        self.user = User.objects.create(
            name='Bill Gates',
            email='bill.gates@hotmail.com',
            password='ilovemicrosoft'
        )

        doctor_schedule = DoctorSchedule.objects.create(
            doctor=self.doctor,
            day='2020-12-10',
        )

        doctor_schedule.available_times.add(
            DoctorScheduleTime.objects.create(time='07:00:00')
        )
        doctor_schedule.available_times.add(
            DoctorScheduleTime.objects.create(time='08:00:00')
        )
        doctor_schedule.available_times.add(
            DoctorScheduleTime.objects.create(time='09:00:00')
        )
        doctor_schedule.available_times.add(
            DoctorScheduleTime.objects.create(time='10:00:00')
        )

    def test_try_to_create_a_appointment_passing_a_past_date(self) -> None:
        """
        Try to create a appointment passing a past date ensuring that the system returns
        the correct error message.
        """
        expected_message = 'You cannot send a past date.'

        with self.assertRaisesMessage(ValidationError, expected_message):
            Appointment.objects.create(
                day='1999-02-01',
                time='07:00:00',
                doctor=self.doctor,
                patient=self.user
            )

    def test_try_to_create_a_appointment_in_a_day_that_the_doctor_does_not_have_schedule(
        self
    ) -> None:
        """
        Try to create a appointment passing a day that the doctor does not have schedule
        ensuring that the system returns the correct error message.
        """
        expected_message = 'This doctor does not have schedule for this day.'

        with self.assertRaisesMessage(ValidationError, expected_message):
            Appointment.objects.create(
                day='2030-12-01',
                time='07:00:00',
                doctor=self.doctor,
                patient=self.user
            )

    def test_try_to_create_a_appointment_in_a_time_that_the_doctor_is_not_available(
        self
    ) -> None:
        """
        Try to create a appointment passing a time where the doctor is not available
        ensuring that the system returns the correct error message.
        """
        expected_message = 'This doctor is not available at this time.'

        with self.assertRaisesMessage(ValidationError, expected_message):
            Appointment.objects.create(
                day='2020-12-10',
                time='20:00:00',
                doctor=self.doctor,
                patient=self.user
            )
