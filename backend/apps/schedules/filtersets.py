"""Contains the Doctor Schedules resource filter sets."""
import django_filters


class DoctorScheduleFilter(django_filters.FilterSet):
    """Define the doctor schedules resource filters."""
    date = django_filters.DateFilter(field_name='day', lookup_expr='exact')
    time = django_filters.TimeFilter(field_name='available_times__time', lookup_expr='exact')
