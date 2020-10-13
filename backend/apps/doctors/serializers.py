"""
Contains the doctors app serializers.

https://www.django-rest-framework.org/api-guide/serializers/
"""

from rest_framework import serializers

from apps.doctors.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    """
    Contains the Doctor Serializer class.
    """

    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ['id']
