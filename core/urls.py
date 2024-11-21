"""
urls.py

Defines the main URL patterns for the Django project.
It includes routes for:
- Admin interface
- App for managing wedding-related functionalities ('noivos')
- App for managing guest interactions ('convidados')
- Serving media files during development
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Admin interface for managing the project
    path('admin/', admin.site.urls),
    
    # URLs for the 'noivos' app (wedding management)
    path('noivos/', include('noivos.urls')),
    
    # URLs for the 'convidados' app (guest interactions)
    path('convidados/', include('convidados.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
Static files and media files are served during development.
MEDIA_URL is the public URL of the media files.
MEDIA_ROOT is the filesystem path where media files are stored.
"""
