"""Contains the Medicar API users app models."""

import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import EmailValidator
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from apps.users.managers import UserManager
from apps.users.signals import generate_user_token


class User(AbstractBaseUser, PermissionsMixin):
    """Define the User model."""
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4
    )
    email = models.EmailField(
        max_length=150,
        unique=True,
        validators=[
            EmailValidator
        ]
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=60,
        blank=True
    )
    date_joined = models.DateTimeField(
        verbose_name=_('date joined'),
        auto_now_add=True
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name=_('staff'),
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name=_('superuser'),
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    class Meta:
        db_table = 'user'

    def save(self, *args, **kwargs) -> None:
        """
        Override the models.Model.save() method to call the
        models.Model.full_clean() method to validate all the fields before
        save.
        """
        self.full_clean()
        super(User, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Return a string representation for a User model instance.
        """
        return self.email


post_save.connect(generate_user_token, sender=User)
