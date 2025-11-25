from logging import raiseExceptions

from django.shortcuts import get_object_or_404

from .models import Client


def get_clients():
    clients = Client.objects.all()
    return clients


def get_client(client_id):
    try:
        client = get_object_or_404(Client, id=client_id)
        return client
    except Client.DoesNotExist:
        return None
