"""
models.py

Defines the data models for the Wedding Manager application:
- Convidados: Represents guests with their details and attendance status.
- Presentes: Represents gifts available for reservation, including details like importance and price.
"""

from django.db import models
import secrets

class Convidados(models.Model):
    """
    Model to represent guests attending the wedding.

    Attributes:
        nome_convidado (str): The name of the guest.
        whatsapp (str): The WhatsApp contact of the guest (optional).
        token (str): A unique token for the guest to access their invitation link.
        status (str): The attendance status of the guest, with choices:
            - 'AC': Awaiting confirmation
            - 'C': Confirmed
            - 'R': Refused
    """
    status_choices = (
        ('AC', 'Aguardando confirmação'),
        ('C', 'Confirmado'),
        ('R', 'Recusado')
    )

    nome_convidado = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=25, null=True, blank=True)
    token = models.CharField(max_length=25)
    status = models.CharField(max_length=2, choices=status_choices, default='AC')

    def save(self, *args, **kwargs):
        """
        Overrides the save method to generate a unique token if not already set.
        """
        if not self.token:
            self.token = secrets.token_urlsafe(16)
        super(Convidados, self).save(*args, **kwargs)

    @property
    def link_convite(self):
        """
        Generates the invitation link for the guest based on their unique token.
        
        Returns:
            str: The URL for the guest's invitation.
        """
        return f'http://127.0.0.1:8000/convidados/?token={self.token}'

    def __str__(self):
        """
        String representation of the guest, showing their name.
        
        Returns:
            str: Guest's name.
        """
        return self.nome_convidado


class Presentes(models.Model):
    """
    Model to represent gifts available for reservation.

    Attributes:
        nome_presente (str): The name of the gift.
        foto (ImageField): An optional image of the gift.
        preco (Decimal): The estimated price of the gift.
        importancia (int): Importance level of the gift, from 1 (low) to 5 (high).
        reservado (bool): Indicates if the gift has been reserved.
        reservado_por (ForeignKey): Links the gift to the guest who reserved it (optional).
    """
    nome_presente = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='presentes')
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    importancia = models.PositiveIntegerField()
    reservado = models.BooleanField(default=False)
    reservado_por = models.ForeignKey(Convidados, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        """
        String representation of the gift, showing its name.
        
        Returns:
            str: Gift's name.
        """
        return self.nome_presente
