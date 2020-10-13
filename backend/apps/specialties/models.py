"""Contains the Medicar API specialties app models."""
import uuid

from django.db import models

from apps.base.models import UUIDTimeControlMethod


class Speciality(UUIDTimeControlMethod):
    """Define the Speciality model."""
    id = models.UUIDField(
        primary_key=True, editable=False, unique=True, default=uuid.uuid4
    )
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        """"""
        return self.name
