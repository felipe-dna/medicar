"""
Contains the users app serializers.

https://www.django-rest-framework.org/api-guide/serializers/
"""
from typing import Dict, Union

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from requests import Request
from rest_framework import serializers

from apps.users.models import User


class LoginSerializer(serializers.Serializer):
    """Define the serializer for the authentication operations."""
    email = serializers.EmailField(
        label="Email",
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, parameters: Dict[str, str]) -> Dict[str, Union[str, User]]:
        """
        Validate the sent parameters when authenticating a user.

        :param parameters: The sent parameters.
        :rtype: Dict[str, str]

        :return: The same given parameters but with the authenticated user inside too.
        :rtype: Dict[str, Union[str, User]]
        """
        email = parameters.get('email')
        password = parameters.get('password')
        request: Request = self.context.get('request')

        if email and password:
            user = authenticate(
                request=request,
                username=email,
                password=password
            )

            if not user:
                error_message = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(error_message, code='authorization')
        else:
            error_message = _('Must include "email" and "password".')
            raise serializers.ValidationError(error_message, code='authorization')

        parameters['user'] = user

        return parameters


class UserSerializer(serializers.ModelSerializer):
    """Define a serialized used in the users resource."""

    password = serializers.CharField(write_only=True)

    def create(self, validated_data) -> User:
        """
        Override the create method to call the User.objects.create_user method.

        :param validated_data: The validated body parameters.
        :type validated_data: Dict[str, Any]

        :return: The created user.
        :rtype: User.
        """
        created_user = User.objects.create_user(**validated_data)
        return created_user

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')
        read_only_fields = ('id',)
