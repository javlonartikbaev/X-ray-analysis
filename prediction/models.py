from django.db import models
from registration.models import Client
from doctors.models import Doctor


# Create your models here.
class Prediction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    prediction = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.client.full_name} - {self.doctor.full_name} - {self.prediction}'
