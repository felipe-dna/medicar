"""
Contains the User model managers.
"""
from typing import Optional

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """"""

    def create_user(self, email: str, password: Optional[str] = None, **kwargs):
        """

        :param email:
        :param password:
        :param kwargs:
        :return:
        """
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email: str, password: str, **kwargs):
        """

        :param email:
        :param password:
        :param kwargs:
        :return:
        """
        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()

        return user
