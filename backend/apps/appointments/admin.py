"""Contains the admin settings for the appointments resource."""
from django.contrib import admin

from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    """Define the admin interface for the appointments resource."""
    fields = ('id', 'day', 'time', 'doctor', 'patient', 'created_at')
    readonly_fields = ('id', 'created_at')


admin.site.register(Appointment, AppointmentAdmin)
