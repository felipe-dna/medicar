"""Contains the Medicar Users app admin configurations."""
from django.contrib import admin

from .models import User

admin.site.register(User)
