"""
Contains the users app urls.

https://www.django-rest-framework.org/api-guide/routers/
"""

from django.urls import path

from apps.users.viewsets import LoginViewSet

app_name = 'users'

urlpatterns = [
    path('users/login', LoginViewSet.as_view(), name='login')
]
