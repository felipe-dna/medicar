"""Contains the DoctorSchedule and DoctorScheduleTime admin settings."""
from django.contrib import admin

from .models import DoctorSchedule, DoctorScheduleTime


class DoctorScheduleTimeAdmin(admin.ModelAdmin):
    """Define the Admin interface settings for the DoctorSchedule model."""
    fields = ('id', 'time', 'created_at')
    readonly_fields = ('id', 'created_at')
    search_fields = ('time',)


class DoctorScheduleAdmin(admin.ModelAdmin):
    """Define the Admin interface settings for the DoctorScheduleTime model."""
    fields = ('id', 'doctor', 'day', 'available_times', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')
    search_fields = ('doctor', 'day', 'available_times')


admin.site.register(DoctorSchedule, DoctorScheduleAdmin)
admin.site.register(DoctorScheduleTime, DoctorScheduleTimeAdmin)
