"""Contains the Doctor resource filter sets."""
import django_filters


class DoctorFilter(django_filters.FilterSet):
    """"""
    speciality = django_filters.UUIDFilter(
        field_name='speciality',
        lookup_expr='exact'
    )
