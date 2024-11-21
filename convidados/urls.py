"""
urls.py

Defines the URL patterns for the Wedding Manager application.
Each URL is linked to a specific view function to handle the associated request.
"""

from django.urls import path
from . import views

# URL patterns for the Wedding Manager app
urlpatterns = [
    # Home page for the application
    # Displays the main page where guests can view wedding information
    path('', views.convidados, name='convidados'),

    # Endpoint for guests to confirm or decline their attendance
    # The response and the guest's unique token must be passed as parameters
    path('responder_presenca/', views.responder_presenca, name='responder_presenca'),

    # Endpoint for reserving a gift for the wedding
    # Uses a dynamic parameter (`<int:id>`) to identify the selected gift
    path('reservar_presente/<int:id>', views.reservar_presente, name='reservar_presente'),
]
