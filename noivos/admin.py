"""
admin.py

Registers models to the Django admin interface, allowing them to be managed through the admin dashboard.
"""

from django.contrib import admin
from .models import Presentes, Convidados

# Register the Presentes model to the admin interface
admin.site.register(Presentes)

# Register the Convidados model to the admin interface
admin.site.register(Convidados)
