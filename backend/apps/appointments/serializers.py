"""
Contains the appointments app serializers.

https://www.django-rest-framework.org/api-guide/serializers/
"""
from drf_writable_nested import WritableNestedModelSerializer

from .models import Appointment
from ..doctors.models import Doctor
from ..specialties.serializers import SpecialityForeignKeySerializer


class AppointmentDoctorSerializer(WritableNestedModelSerializer):
    """Define a serializer used to get the doctor data when looking for appointments."""
    speciality = SpecialityForeignKeySerializer(many=False)

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'crm', 'speciality')
        read_only_fields = ('id', 'created_at', 'updated_at', 'speciality')


class AppointmentSerializer(WritableNestedModelSerializer):
    """Define a serialized used in the appointment resource."""
    doctor = AppointmentDoctorSerializer(many=False)

    class Meta:
        model = Appointment
        fields = ('id', 'doctor', 'day', 'time', 'created_at')
        read_only_fields = ('id', 'patient', 'updated_at')
