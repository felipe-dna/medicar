"""
Contains the doctors app view sets.

https://www.django-rest-framework.org/api-guide/viewsets/
"""

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from ..schedules.filtersets import DoctorScheduleFilter
from ..schedules.models import DoctorSchedule
from ..schedules.serializers import DoctorScheduleSerializer
from .filtersets import DoctorFilter
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    """Contains the Doctor view set."""
    http_method_names = ('options', 'post', 'get', 'patch', 'delete')
    permission_classes = (IsAuthenticated,)
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    # Filter settings.
    # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_class = DoctorFilter
    search_fields = ('name',)

    @action(
        detail=True,
        methods=['get'],
        permission_classes=[IsAuthenticated],
        url_path='schedules'
    )
    def get_doctor_schedules(self, _: Request, pk: str) -> Response:
        """
        Manages the doctors/<pk/schedules resource.

        Checks if the given user exists calling the retrieve method and then, tries to get
        the doctor schedules filtering by the given doctor id(pk). Finally, returns it as
        response.

        :param _: The HTTP response object.
        :type _: rest_framework.request.Request.

        :param pk: The doctor id passed in the path.
        :type pk: str.

        :return: A rest_framework.response.Response object with the serialized data.
        :rtype: rest_framework.response.Response.
        """
        self.queryset = DoctorSchedule.objects.filter(doctor__id=pk)
        self.filterset_class = DoctorScheduleFilter

        doctor_schedule = self.filter_queryset(self.queryset)

        self.serializer_class = DoctorScheduleSerializer

        serializer = self.get_serializer(doctor_schedule, many=True)
        response = Response(serializer.data)

        return response
