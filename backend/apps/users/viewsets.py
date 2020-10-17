"""
Contains the users app view sets.

https://www.django-rest-framework.org/api-guide/viewsets/
"""

from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema

from apps.users.serializers import LoginSerializer


class LoginViewSet(ObtainAuthToken):
    """Define the login view set."""
    serializer_class = LoginSerializer
    http_method_names = ['post']

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description=_("Valid email for authentication"),
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title=_("Password"),
                        description=_("Valid password for authentication"),
                    ),
                ),
            ],
            encoding="application/json",
        )
