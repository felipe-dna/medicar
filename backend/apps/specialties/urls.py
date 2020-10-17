"""
Contains the specialties app urls.

https://www.django-rest-framework.org/api-guide/routers/
"""

from django.urls import include, path
from rest_framework import routers

from .viewsets import SpecialityViewSet

app_name = 'specialties'

router = routers.SimpleRouter(trailing_slash=False)
router.register('specialties', SpecialityViewSet)

urlpatterns = [
    path('', include(router.urls))
]
