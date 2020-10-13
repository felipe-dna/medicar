"""Contains the Medicar API users app models."""
from django.db import models

from apps.base.models import UUIDTimeControlMethod
from apps.doctors.models import Doctor
from apps.schedules.validators import validate_schedule_date


class DoctorScheduleTime(UUIDTimeControlMethod):
    """Define the ScheduleTime model."""
    time = models.TimeField()

    class Meta:
        db_table = 'doctor_schedule_time'

    def save(self, *args, **kwargs) -> None:
        """
        Override the models.Model.save() method to call the
        models.Model.full_clean() method to validate all the fields before
        save.
        """
        self.full_clean()
        super(DoctorScheduleTime, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Return a string representation for a DoctorScheduleTime model instance.
        """
        return self.time.strftime('%HH:%MM:%SS')


class DoctorSchedule(UUIDTimeControlMethod):
    """Define the DoctorSchedule model."""
    doctor = models.ForeignKey(
        to=Doctor,
        on_delete=models.CASCADE
    )
    day = models.DateField(
        validators=[
            validate_schedule_date
        ]
    )
    available_times = models.ManyToManyField(
        to=DoctorScheduleTime,
        blank=True
    )

    class Meta:
        # https://docs.djangoproject.com/en/3.1/ref/models/options/#unique-together
        unique_together = [['doctor', 'day']]
        db_table = 'doctor_schedule'

    def save(self, *args, **kwargs) -> None:
        """
        Override the models.Model.save() method to call the
        models.Model.full_clean() method to validate all the fields before
        save.
        """
        self.full_clean()
        super(DoctorSchedule, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Return a string representation for a DoctorSchedule model instance.
        """
        return f'Dr. {self.doctor.name} - {self.day.strftime("%dd/mm/YY")}'

