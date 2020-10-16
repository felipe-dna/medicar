"""Contains the schedules app validators."""
from datetime import date

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_schedule_date(time_value: date) -> None:
    """
    Checks if the current time value it's a past date.

    :param time_value: The current time value.
    :type time_value: datetime.date.
    """
    if time_value < date.today():
        raise ValidationError(_("You cannot send a past date."))
