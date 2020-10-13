"""
Contains the doctors app serializers.

https://www.django-rest-framework.org/api-guide/serializers/
"""

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from apps.doctors.models import Doctor
from apps.specialties.models import Speciality


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'name']
        read_only_fields = ['name']


class DoctorSerializer(WritableNestedModelSerializer):
    """
    Contains the Doctor Serializer class.
    """
    speciality = SpecialitySerializer(many=False)

    class Meta:
        model = Doctor
        fields = [
            'id', 'name', 'crm', 'email', 'phone', 'speciality', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'speciality']
