"""Contains the Medicar API doctors app models."""
from django.core.validators import EmailValidator
from django.db import models

from django.utils.translation import ugettext_lazy as _

from apps.base.models import UUIDTimeControlMethod
from apps.specialties.models import Speciality


class Doctor(UUIDTimeControlMethod):
    """Define the Doctor model."""
    name = models.CharField(
        verbose_name=_('name'),
        max_length=60
    )
    crm = models.PositiveIntegerField(
        max_length=4,
        unique=True
    )
    email = models.EmailField(
        max_length=150,
        unique=True,
        validators=[
            EmailValidator
        ]
    )
    phone = models.CharField(
        verbose_name=_('phone'),
        max_length=11
    )
    speciality = models.ForeignKey(
        to=Speciality,
        verbose_name=_('speciality'),
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs) -> None:
        """
        Override the models.Model.save() method to call the
        models.Model.full_clean() method to validate all the fields before
        save.
        """
        self.full_clean()
        super(Doctor, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Return a string representation for a User model instance.
        """
        return f"Dr. {self.name}"
