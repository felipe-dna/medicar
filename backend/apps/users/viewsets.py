"""
Contains the users app view sets.

https://www.django-rest-framework.org/api-guide/viewsets/
"""

from rest_framework.authtoken.views import ObtainAuthToken

from apps.users.serializers import LoginSerializer


class LoginViewSet(ObtainAuthToken):
    """Define the login view set."""
    serializer_class = LoginSerializer
    http_method_names = ['post']
