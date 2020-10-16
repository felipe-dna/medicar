"""
Contains the Medicar API urls settings.
TODO: add path to docs.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Admin urls.
    path('admin/', admin.site.urls),

    # API urls.
    path('v1/', include('apps.doctors.urls'), name='doctors'),
    path('v1/', include('apps.specialties.urls'), name='specialties'),
]

# Static and media URLS settings.
# https://docs.djangoproject.com/en/3.1/howto/static-files/
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
