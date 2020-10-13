"""
Contains the doctors app urls.

https://www.django-rest-framework.org/api-guide/routers/
"""

from django.urls import include, path
from rest_framework import routers

from .viewsets import DoctorViewSet

app_name = 'doctors'

router = routers.SimpleRouter(trailing_slash=False)
router.register('doctors', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls))
]
