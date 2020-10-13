"""Contains the Medicar API specialties app models."""
from django.db import models

from apps.base.models import UUIDTimeControlMethod


class Speciality(UUIDTimeControlMethod):
    """Define the Speciality model."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        """Return a string representation for Speciality model instance."""
        return self.name
