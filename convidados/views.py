"""
views.py

Handles the core functionalities of the Wedding Manager application:
- Displaying guest information and available gifts.
- Allowing guests to confirm attendance or reserve gifts.
"""

from django.shortcuts import render, redirect
from noivos.models import Convidados, Presentes

def convidados(request):
    """
    Displays the main page for a guest, including their information and a list of available gifts.

    Args:
        request (HttpRequest): The HTTP request object containing the 'token' parameter.

    Returns:
        HttpResponse: Renders the 'convidados.html' template with:
            - convidado: The guest's information.
            - presentes: A list of unreserved gifts, sorted by importance.
            - token: The guest's unique token.
    """
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)
    presentes = Presentes.objects.filter(reservado=False).order_by('-importancia')
    return render(request, 'convidados.html', {'convidado': convidado, 'presentes': presentes, 'token': token})

def responder_presenca(request):
    """
    Allows a guest to confirm or decline their attendance at the wedding.

    Args:
        request (HttpRequest): The HTTP request object containing:
            - 'resposta': The guest's response ('C' for confirm, 'R' for decline).
            - 'token': The guest's unique token.

    Returns:
        HttpResponse: Redirects to the 'convidados' page with the guest's token.
    """
    resposta = request.GET.get('resposta')
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)

    # Redirect back to the guest page if the response is invalid
    if resposta not in ['C', 'R']:
        return redirect(f'/convidados/?token={token}')
    
    # Update the guest's attendance status
    convidado.status = resposta
    convidado.save()

    return redirect(f'/convidados/?token={token}')

def reservar_presente(request, id):
    """
    Allows a guest to reserve a gift.

    Args:
        request (HttpRequest): The HTTP request object containing:
            - 'token': The guest's unique token.
        id (int): The ID of the gift to be reserved.

    Returns:
        HttpResponse: Redirects to the 'convidados' page with the guest's token.
    """
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)
    presente = Presentes.objects.get(id=id)
    
    # Mark the gift as reserved and associate it with the guest
    presente.reservado = True
    presente.reservado_por = convidado
    presente.save()

    return redirect(f'/convidados/?token={token}')
