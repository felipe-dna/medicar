"""
Contains the users app view sets.

https://www.django-rest-framework.org/api-guide/viewsets/
"""
from typing import List, Type

from django.db.models import QuerySet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission

from apps.users.models import User
from apps.users.serializers import LoginSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Define the users view set."""

    http_method_names = ['get', 'post']
    serializer_class = UserSerializer

    def get_permissions(self) -> List[Type[BasePermission]]:
        """
        Override the get_permissions method to define the self._permission_classes for each request type.

        :return: A list of permissions classes instances.
        :rtype: List[Type[BasePermission]].
        """
        permissions = [IsAuthenticated()] if self.request.method == 'GET' else []
        return permissions

    def get_queryset(self) -> QuerySet:
        """
        Override the get_queryset method to return the defined queryset for each request type.

        :return: The correct queryset for each request type.
        :rtype: QuerySet.
        """
        if self.request.method == 'GET':
            user = self.request.user
            queryset = User.objects.filter(id=user.id)
        else:
            queryset = User.objects.all()

        return queryset


class LoginViewSet(ObtainAuthToken):
    """Define the login view set."""
    serializer_class = LoginSerializer
    http_method_names = ['post']
