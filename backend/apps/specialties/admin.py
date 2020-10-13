"""Contains the Medicar Specialties app admin configurations."""
from django.contrib import admin

from .models import Speciality

admin.site.register(Speciality)
