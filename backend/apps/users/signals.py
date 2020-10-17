"""Contain the users apps signals."""
from rest_framework.authtoken.models import Token


def generate_user_token(sender, instance, created: bool, **kwargs) -> None:
    """
    Called when a new user is created, it generate a new Token for this user.

    :param sender: The model class that just had an instance created.
    :type sender: users.models.User.
    :param instance: The created user instance.
    :type instance: users.models.User.
    :param created: A boolean value that defines if the user is being created or updated.
    :type created: bool
    """
    if created:
        Token.objects.create(user=instance)
