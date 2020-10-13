"""
Contains the doctors app validators.

https://docs.djangoproject.com/en/3.1/ref/validators/
"""

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_crm(value: str) -> None:
    """
    Apply some validations in the crm field.

    :param value: The current crm value.
    """

    if not value.isdigit():
        raise ValidationError(_("The CRM must be a numeric value."))


def validate_phone(value: str) -> None:
    """
    Apply some validations in the phone field.

    :param value: The current phone value.
    """

    if not value.isdigit():
        raise ValidationError(_("The phone must be a numeric value."))

    if len(value) < 10:
        raise ValidationError(_("A phone number must have at least 8 characters."))
