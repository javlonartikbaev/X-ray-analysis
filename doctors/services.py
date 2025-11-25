from django.db import transaction

from .models import Doctor


@transaction.atomic
def create_doctor(full_name: str,
                  phone_number: str,
                  password: str,
                  **fields):
    doctor = Doctor.objects.create_user(
        full_name=full_name,
        phone_number=phone_number,
    )
    img = fields.get('img')
    if img is not None:
        doctor.img = fields['img']
    doctor.set_password(password)
    doctor.full_clean()
    doctor.save()
    return doctor
