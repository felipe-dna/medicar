"""Contains the Medicar Specialties app admin configurations."""

from django.contrib import admin

from .models import Speciality


class SpecialityAdmin(admin.ModelAdmin):
    """Define the admin functionalities for the Speciality app."""
    fields = ('id', 'name', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Speciality, SpecialityAdmin)
