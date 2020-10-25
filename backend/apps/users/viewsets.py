"""
Contains the users app view sets.

https://www.django-rest-framework.org/api-guide/viewsets/
"""
from django.db.models import QuerySet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.serializers import LoginSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """"""
    http_method_names = ['get']
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self) -> QuerySet:
        """"""
        user = self.request.user
        queryset = User.objects.filter(id=user.id)

        return queryset


class LoginViewSet(ObtainAuthToken):
    """Define the login view set."""
    serializer_class = LoginSerializer
    http_method_names = ['post']
