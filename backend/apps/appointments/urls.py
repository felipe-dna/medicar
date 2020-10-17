"""
Contains the appointments app urls.

https://www.django-rest-framework.org/api-guide/routers/
"""

from django.urls import include, path
from rest_framework import routers

from .viewsets import AppointmentViewSet

app_name = 'appointments'

router = routers.SimpleRouter(trailing_slash=False)
router.register('appointments', AppointmentViewSet, basename='appointments')

urlpatterns = [
    path('', include(router.urls))
]
