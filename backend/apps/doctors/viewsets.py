"""
Contains the doctors app view sets.

https://www.django-rest-framework.org/api-guide/viewsets/
"""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .filtersets import DoctorFilter
from .models import Doctor
from .serializers import DoctorSerializer
from ..schedules.models import DoctorSchedule
from ..schedules.serializers import DoctorScheduleSerializer


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

    @action(detail=True, methods=['get'], permission_classes=[], url_path='schedules')
    def get_doctor_schedules(self, request: Request, pk: str) -> Response:
        """
        Manages the doctors/<pk/schedules resource.

        Checks if the given user exists calling the retrieve method and then, tries to get
        the doctor schedules filtering by the given doctor id(pk). Finally, returns it as
        response.

        :param request: The HTTP response object.
        :type request: rest_framework.request.Request.

        :param pk: The doctor id passed in the path.
        :type pk: str.

        :return: A rest_framework.response.Response object with the serialized data.
        :rtype: rest_framework.response.Response.
        """
        self.retrieve(request=request, pk=pk)

        doctor_schedule = DoctorSchedule.objects.filter(doctor__id=pk)

        self.serializer_class = DoctorScheduleSerializer
        serializer = self.get_serializer(doctor_schedule, many=True)

        response = Response(serializer.data)

        return response
