""""""
import uuid

from django.db import models

from apps.base.models import UUIDTimeControlMethod
from apps.specialties.models import Speciality


class Doctor(UUIDTimeControlMethod):
    """"""
    id = models.UUIDField(
        primary_key=True, editable=False, unique=True, default=uuid.uuid4
    )
    name = models.CharField(max_length=100)
    crm = models.CharField(max_length=160, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=11)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Dr. {self.name}"
