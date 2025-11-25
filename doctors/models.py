from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class DoctorManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('User must have phone number')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Doctor(AbstractBaseUser):
    full_name = models.CharField()
    phone_number = models.CharField(unique=True)
    password = models.CharField()
    img = models.ImageField(upload_to='doctors/', null=True, blank=True)

    objects = DoctorManager()
    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.full_name
