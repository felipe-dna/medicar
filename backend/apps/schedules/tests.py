"""
Contains the schedules app tests.

https://docs.djangoproject.com/en/3.1/topics/testing/overview/
"""

from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase

from ..doctors.models import Doctor
from ..specialties.models import Speciality
from .models import DoctorSchedule, DoctorScheduleTime


class DoctorScheduleTimeModelTestCase(TestCase):
    """Define the doctor schedule time model tests."""

    def test_create_a_schedule_time_passing_wrong_time_format(self) -> None:
        """
        Try to create a schedule time passing wrong time format ensuring
        that the system returns a ValidationError exception with the correct
        error message.
        """
        invalid_time_format = "a invalid time format"
        expected_message = f"{invalid_time_format}” value has an invalid " \
                           f"format. It must be in HH:MM[:ss[.uuuuuu]] format."

        with self.assertRaisesMessage(ValidationError, str(expected_message)):
            DoctorScheduleTime.objects.create(time=invalid_time_format)


class DoctorScheduleModelTestCase(TestCase):
    """Define the doctor schedule model tests."""

    def setUp(self) -> None:
        """Set up the environment for this test class."""
        speciality = Speciality.objects.create(
            name="pediatrics"
        )

        self.doctor = Doctor.objects.create(
            name="John Doe",
            crm=4445,
            email="john@doe.com",
            phone=12345678901,
            speciality=speciality
        )

        self.second_doctor = Doctor.objects.create(
            name="Joan Doe",
            crm=3333,
            email="joan@doe.com",
            phone=83999999999,
            speciality=speciality
        )

        self.schedule_time = DoctorScheduleTime.objects.create(
            time='13:00:00',
        )

    def test_create_a_doctor_schedule_passing_correct_fields(self) -> None:
        """
        Try to create a DoctorSchedule register passing correct parameters and
        ensuring that the data was inserted correctly.
        """

        created_doctor_schedule = DoctorSchedule.objects.create(
            doctor=self.doctor,
            day=datetime.now(),
        )

        created_doctor_schedule.available_times.add(self.schedule_time)

        filtered_doctor_schedules = DoctorSchedule.objects.filter(
            id=created_doctor_schedule.id
        )

        self.assertTrue(filtered_doctor_schedules.exists())

        self.assertTrue(
            self.schedule_time in
            filtered_doctor_schedules[0].available_times.all()
        )

    def test_try_to_schedule_two_doctors_to_the_same_day(self) -> None:
        """
        Try to schedule two doctors to the same day ensuring that the system is
        raising a ValidationError and returning the correct error message.
        """

        expected_message = "Doctor schedule with this Doctor and Day already exists."

        DoctorSchedule.objects.create(
            doctor=self.doctor,
            day=datetime.now().date(),
        )

        with self.assertRaisesMessage(ValidationError, expected_message):
            DoctorSchedule.objects.create(
                doctor=self.doctor,
                day=datetime.now().date(),
            )

    def test_try_to_create_a_schedule_passing_a_past_date(self) -> None:
        """
        Try to create a schedule passing a past date, ensuring that the system
        is raising a ValidationError and returning the correct message.
        """

        expected_message = "You cannot send a past date."
        wrong_date_format = datetime.now().date() - timedelta(days=10)

        with self.assertRaisesMessage(ValidationError, expected_message):
            DoctorSchedule.objects.create(
                doctor=self.doctor,
                day=wrong_date_format,
            )
