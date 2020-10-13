"""
Contains the users app serializers.

https://www.django-rest-framework.org/api-guide/serializers/
"""
from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Define the User """

    class Meta:
        fields = '__all__'
        model = User
