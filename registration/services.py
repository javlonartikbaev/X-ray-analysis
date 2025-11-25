from django.db import transaction
from rest_framework.generics import get_object_or_404

from .models import Client
from .selectors import get_client, get_clients


@transaction.atomic
def create_client(*, full_name: str,
                  phone_number: str,
                  passport_seria: str,
                  passport_pinfl: str,
                  date_of_birth,
                  gender):
    client = Client(full_name=full_name, phone_number=phone_number, passport_seria=passport_seria,
                    passport_pinfl=passport_pinfl, date_of_birth=date_of_birth, gender=gender)
    client.full_clean()
    client.save()
    return client


@transaction.atomic
def update_client(*, client_id: int, **fields):
    try:
        client = get_object_or_404(Client, pk=client_id)
        for key, value in fields.items():
            setattr(client, key, value)
        client.full_clean()
        client.save()
        return client
    except Client.DoesNotExist:
        return None


@transaction.atomic
def delete_client(*, client_id: int):
    try:
        client = get_client(client_id)
        client.delete()
        return client
    except Client.DoesNotExist:
        return None
