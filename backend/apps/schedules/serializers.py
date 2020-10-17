"""
Contains the schedules app serializers.

https://www.django-rest-framework.org/api-guide/serializers/
"""

from rest_framework import serializers

from .models import DoctorSchedule, DoctorScheduleTime


class DoctorScheduleTimeSerializer(serializers.ModelSerializer):
    """Contains the Schedule Time Serializer class."""

    class Meta:
        model = DoctorScheduleTime
        fields = ['id', 'time']
        read_only_fields = ['id', 'time', 'created_at']


class DoctorScheduleSerializer(serializers.ModelSerializer):
    """Contains the Schedule Serializer class."""
    available_times = DoctorScheduleTimeSerializer(many=True)

    class Meta:
        model = DoctorSchedule
        fields = ['id', 'doctor', 'day', 'available_times', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'doctor']
