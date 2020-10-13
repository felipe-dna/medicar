"""
Contains the users app view sets.

https://www.django-rest-framework.org/api-guide/viewsets/
"""

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from apps.users.models import User
from apps.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
