""""""
from django.contrib import admin

from .models import DoctorSchedule, DoctorScheduleTime

admin.site.register(DoctorSchedule)
admin.site.register(DoctorScheduleTime)
