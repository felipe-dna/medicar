"""
Contains the Specialties app serializers.

https://www.django-rest-framework.org/api-guide/serializers/
"""

from rest_framework import serializers

from .models import Speciality


class SpecialitySerializer(serializers.ModelSerializer):
    """Define the serializer class used to read and create specialties."""
    class Meta:
        model = Speciality
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class SpecialityForeignKeySerializer(serializers.ModelSerializer):
    """Define the serializer object used to read and set a speciality to/from a Doctor."""
    class Meta:
        model = Speciality
        fields = ['id', 'name']
        read_only_fields = ['name']
