"""Contains the Medicar API specialties app models."""
from django.db import models

from apps.base.models import UUIDTimeControlMethod


class Speciality(UUIDTimeControlMethod):
    """Define the Speciality model."""
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'speciality'

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Speciality, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """Return a string representation for Speciality model instance."""
        return self.name
