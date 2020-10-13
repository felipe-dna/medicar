from datetime import date

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_schedule_date(value: date) -> None:
    """"""
    if value < date.today():
        raise ValidationError(_("You cannot send a past date."))
