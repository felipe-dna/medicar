"""
Contains the doctors app view sets.

https://www.django-rest-framework.org/api-guide/viewsets/
"""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .filtersets import DoctorFilter
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    """Contains the Doctor view set."""

    http_method_names = ('options', 'post', 'get', 'patch', 'delete')
    permission_classes = []
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    # Filter settings.
    # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_class = DoctorFilter
    search_fields = ('name',)
