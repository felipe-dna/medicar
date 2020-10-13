"""Contains the base model used in the other models."""
import uuid

from django.db import models


class UUIDTimeControlMethod(models.Model):
    """
    Define a abstract model that provides a uuid, created_at and updated_at
    fields.
    """
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
