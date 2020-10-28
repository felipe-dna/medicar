"""
Contains the appointments app serializers.

https://www.django-rest-framework.org/api-guide/serializers/
"""
from django.db.models import QuerySet
from rest_framework import serializers

from rest_framework.exceptions import NotFound

from .models import Appointment
from ..doctors.models import Doctor
from ..specialties.serializers import SpecialityForeignKeySerializer
from ..users.models import User


class AppointmentDoctorSerializer(serializers.ModelSerializer):
    """Define a serializer used to get the doctor data when looking for appointments."""
    speciality = SpecialityForeignKeySerializer(many=False, read_only=True)

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'crm', 'speciality')
        read_only_fields = ('id', 'created_at', 'updated_at', 'speciality', 'name', 'crm', 'speciality')


class AppointmentSerializer(serializers.ModelSerializer):
    """Define a serialized used in the appointment resource."""
    doctor = AppointmentDoctorSerializer(many=False, read_only=True, required=False)
    patient_id = serializers.CharField(write_only=True)
    doctor_id = serializers.CharField(write_only=True)
    time = serializers.TimeField(format='%H:%M')

    class Meta:
        model = Appointment
        fields = ('id', 'doctor', 'day', 'time', 'created_at', 'doctor_id', 'patient_id')
        read_only_fields = ('id', 'patient', 'updated_at', 'created_at')

    def create(self, validated_data):
        doctor: QuerySet[Doctor] = Doctor.objects.filter(id=validated_data.get('doctor_id'))
        patient: QuerySet[User] = User.objects.filter(id=validated_data.get('patient_id'))

        if not doctor.exists():
            raise NotFound(detail='Doctor not found')
        if not patient.exists():
            raise NotFound(detail='Patient not found')

        created_appointment = Appointment.objects.create(
            day=validated_data.get('day'),
            time=validated_data.get('time'),
            doctor=doctor[0],
            patient=patient[0]
        )

        return created_appointment
