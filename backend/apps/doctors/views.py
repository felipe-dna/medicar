"""Contains the Medicar API doctors app models."""
import uuid

from django.db import models


class MedicalSpeciality(models.Model):
    """Define the Me."""
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Doctor(models.Model):
    """Define the Doctor model."""
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=120)
    crm = models.PositiveIntegerField(max_length=7)
