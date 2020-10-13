"""
Contains the User model managers.
"""
from typing import Optional, Type

from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Defines a object manager to the User model."""

    def create_user(
            self, email: str, password: Optional[str] = None, **kwargs
    ) -> Type[models.Model]:
        """
        Create a new user in the database.

        Receives the email and password first to set it manually. The password
        must be inserted via model.set_password() to ensure the security.
        Then, the rest of the parameters are inserted bia kwargs and the user
        instance is inserted using the method user.save(). Finally, the created
        user is returned.

        :param email: The email of the user that will be saved.
        :param password: The password of the user that will be saved.
        :param kwargs: The rest of the parameters used to create a new user.

        :return: A User model instance.
        """
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(
            self, email: str, password: str, **kwargs
    ) -> Type[models.Model]:
        """
        Create a new super user in the database.

        Receives the email and password first to set it manually. Also, we
        set up the is_admin and is_staff as True (only to admin). The password
        must be inserted via model.set_password() to ensure the security.
        Then, the rest of the parameters are inserted bia kwargs and the user
        instance is inserted using the method user.save(). Finally, the created
        user is returned.

        :param email: The email of the user that will be saved.
        :param password: The password of the user that will be saved.
        :param kwargs: The rest of the parameters used to create a new user.
        """
        user = self.model(
            email=email, is_staff=True, is_superuser=True, **kwargs
        )
        user.set_password(password)
        user.save()

        return user
