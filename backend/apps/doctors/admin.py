"""Contains the Medicar Doctors app admin configurations."""

from django.contrib import admin

from .models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    """Define the admin functionalities fir the Doctors app."""
    fields = (
        'id', 'name', 'crm', 'email', 'phone', 'speciality', 'created_at', 'updated_at'
    )
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Doctor, DoctorAdmin)
