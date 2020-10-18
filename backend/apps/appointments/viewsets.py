"""
Contains the appointments app view sets.

https://www.django-rest-framework.org/api-guide/viewsets/
"""
from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    """Define the appointments resource view set."""
    http_method_names = ('options', 'get', 'post', 'delete')
    permission_classes = (IsAuthenticated,)
    serializer_class = AppointmentSerializer

    def get_queryset(self) -> QuerySet[Appointment]:
        """Overrides the get_queryset method to make it list just the user appointment."""
        return Appointment.objects.filter(patient=self.request.user)
