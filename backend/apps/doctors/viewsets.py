"""
Contains the doctors app view sets.

https://www.django-rest-framework.org/api-guide/viewsets/
"""

from rest_framework import viewsets

from apps.doctors.models import Doctor
from apps.doctors.serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    """Contains the Doctor view set."""

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = []
    http_method_names = ['options', 'post', 'get', 'patch', 'delete']
