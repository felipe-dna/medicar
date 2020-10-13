""""""
import uuid

from django.db import models

from apps.base.models import UUIDTimeControlMethod
from apps.doctors.models import Doctor
from apps.schedules.validators import validate_schedule_date


class DoctorScheduleTime(UUIDTimeControlMethod):
    id = models.UUIDField(
        primary_key=True, editable=False, unique=True, default=uuid.uuid4
    )
    time = models.TimeField()

    def __str__(self) -> str:
        return self.time.strftime('%HH:%MM:%SS')


class DoctorSchedule(UUIDTimeControlMethod):
    """"""
    id = models.UUIDField(
        primary_key=True, editable=False, unique=True, default=uuid.uuid4
    )
    doctor = models.ForeignKey(to=Doctor, on_delete=models.CASCADE)
    day = models.DateField(validators=[validate_schedule_date])
    available_times = models.ManyToManyField(to=DoctorScheduleTime, blank=True)

    class Meta:
        """"""
        # https://docs.djangoproject.com/en/3.1/ref/models/options/#unique-together
        unique_together = [['doctor', 'day']]

    def __str__(self) -> str:
        """"""
        return f'Dr. {self.doctor.name} - {self.day.strftime("%dd/mm/YY")}'

