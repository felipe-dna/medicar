"""Contains the Medicar API specialties app models."""
from django.db import models

from apps.base.models import UUIDTimeControlModel


class Speciality(UUIDTimeControlModel):
    """Define the Speciality model."""
    name = models.CharField(
        max_length=100,
        unique=True
    )

    class Meta:
        db_table = 'speciality'
        verbose_name = 'speciality'
        verbose_name_plural = 'specialties'

    def save(self, *args, **kwargs) -> None:
        """
        Override the models.Model.save() method to call the
        models.Model.full_clean() method to validate all the fields before
        save.
        """
        self.full_clean()
        super(Speciality, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """Return a string representation for Speciality model instance."""
        return self.name
