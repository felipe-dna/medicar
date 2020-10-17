"""Contains the Medicar  appointments app models."""

from django.db import models
from django.db.models import QuerySet
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from ..base.models import UUIDTimeControlModel
from ..doctors.models import Doctor
from ..schedules.models import DoctorSchedule, DoctorScheduleTime
from ..schedules.validators import validate_schedule_date
from ..users.models import User


class Appointment(UUIDTimeControlModel):
    """Define the Medical Appointment model."""
    day = models.DateField(
        verbose_name=_('day'),
        validators=[
            validate_schedule_date
        ]
    )
    time = models.TimeField(
        verbose_name=_('time')
    )
    doctor = models.ForeignKey(
        to=Doctor,
        on_delete=models.CASCADE
    )
    patient = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'medical_appointment'

    def clean(self) -> None:
        """Apply some validations in the fields following the business logic."""
        doctor_schedule: QuerySet[DoctorSchedule] = DoctorSchedule.objects.filter(
            doctor=self.doctor,
            day=self.day
        )

        if not doctor_schedule.exists():
            raise ValidationError(_("This doctor does not have schedule for this day."))

        if not doctor_schedule[0].available_times.filter(time=self.time).exists():
            raise ValidationError(_("This doctor is not available at this time."))

    def save(self, *args, **kwargs) -> None:
        """
        Override the models.Model.save() method to call the
        models.Model.full_clean() method to validate all the fields before
        save.
        """
        self.full_clean()
        super(Appointment, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Return a string representation for a Appointment model instance.
        """
        return f'Dr. {self.doctor.name} - {self.day.strftime("%d/%m/%Y")}'

