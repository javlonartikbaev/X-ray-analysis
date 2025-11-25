from django.db import models


# Create your models here.
class Client(models.Model):
    class Gender(models.TextChoices):
        MALE = 'мужчина'
        FEMALE = 'женщина'

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    passport_seria = models.CharField(max_length=9)
    passport_pinfl = models.CharField(max_length=14)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=Gender.choices)

    class Meta:
        db_table = 'client'
        verbose_name_plural = 'Clients'
