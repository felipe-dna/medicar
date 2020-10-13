"""Contains the Doctor resource filter sets."""
import django_filters


class DoctorFilter(django_filters.FilterSet):
    """Define the doctors resource filters."""
    speciality = django_filters.UUIDFilter(
        field_name='speciality',
        lookup_expr='exact'
    )
