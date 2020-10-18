"""
Contains the doctors app serializers.

https://www.django-rest-framework.org/api-guide/serializers/
"""

from drf_writable_nested import WritableNestedModelSerializer

from ..specialties.serializers import SpecialityForeignKeySerializer
from .models import Doctor


class DoctorSerializer(WritableNestedModelSerializer):
    """Contains the Doctor Serializer class."""
    speciality = SpecialityForeignKeySerializer(many=False)

    class Meta:
        model = Doctor
        fields = (
            'id', 'name', 'crm', 'email', 'phone', 'speciality', 'created_at',
            'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at', 'speciality')
