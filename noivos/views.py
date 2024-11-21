"""
views.py

Contains the views for the 'noivos' app in the Wedding Manager application.
Handles rendering pages and processing requests related to gifts and guest management.
"""

from django.shortcuts import render, redirect
from .models import Presentes, Convidados

def home(request):
    """
    Handles the homepage logic for managing gifts.

    GET:
        Retrieves all gifts and calculates the count of reserved and unreserved gifts.
        Renders the 'home.html' template with:
            - 'presentes': List of all gifts.
            - 'data': List containing counts of reserved and unreserved gifts.
    
    POST:
        Creates a new gift based on the submitted form data.
        Validates the 'importance' field (must be between 1 and 5).
        Redirects back to the homepage after saving the new gift.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders 'home.html' or redirects to 'home'.
    """
    if request.method == "GET":
        presentes = Presentes.objects.all()
        nao_reservado = Presentes.objects.filter(reservado=False).count()
        reservado = Presentes.objects.filter(reservado=True).count()
        data = [nao_reservado, reservado]
        return render(request, 'home.html', {'presentes': presentes, 'data': data})
    
    elif request.method == "POST":
        nome_presente = request.POST.get('nome_presente')
        foto = request.FILES.get('foto')
        preco = request.POST.get('preco')
        importancia = int(request.POST.get('importancia'))

        if importancia < 1 or importancia > 5:
            return redirect('home')

        presentes = Presentes(
            nome_presente=nome_presente,
            foto=foto,
            preco=preco,
            importancia=importancia,
        )

        presentes.save()

        return redirect('home')
    
def lista_convidados(request):
    """
    Handles the logic for managing the guest list.

    GET:
        Retrieves all registered guests and renders the 'lista_convidados.html' template.
        Passes the list of guests to the template.

    POST:
        Creates a new guest based on the submitted form data.
        Redirects to the 'lista_convidados' page after saving the guest.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders 'lista_convidados.html' or redirects to 'lista_convidados'.
    """
    if request.method == 'GET':
        convidados = Convidados.objects.all()
        return render(request, 'lista_convidados.html', {'convidados': convidados})
    
    elif request.method == 'POST':
        nome_convidado = request.POST.get('nome_convidado')
        whatsapp = request.POST.get('whatsapp')

        convidados = Convidados(
            nome_convidado=nome_convidado,
            whatsapp=whatsapp
        )

        convidados.save()

        return redirect('lista_convidados')
