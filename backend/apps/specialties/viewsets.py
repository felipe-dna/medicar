"""
Contains the specialties app view sets.

https://www.django-rest-framework.org/api-guide/viewsets/
"""

from rest_framework import filters, viewsets

from .models import Speciality
from .serializers import SpecialitySerializer


class SpecialityViewSet(viewsets.ModelViewSet):
    """Contains the Speciality view set."""

    http_method_names = ('options', 'post', 'get')
    permission_classes = []
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

    # Filter settings.
    # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
