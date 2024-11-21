"""
urls.py

Defines the URL patterns for the 'noivos' app in the Wedding Manager application.
Routes requests to views for managing wedding details like guests and gifts.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page for the application
    # Displays an overview of wedding management, including gifts and guest details
    path('', views.home, name='home'),
    
    # Guest list management page
    # Allows viewing and adding new guests
    path('lista_convidados', views.lista_convidados, name='lista_convidados'),
]
