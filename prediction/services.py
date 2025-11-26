from .models import Prediction
from registration.models import Client
from doctors.models import Doctor
from ai_model.analysis import analysis


def create_prediction(client, img, doctor):
    ai_response = analysis(img)
    prediction = Prediction(client=client, prediction=ai_response, img=img, doctor=doctor)
    prediction.full_clean()
    prediction.save()
    return prediction


def get_prediction():
    prediction = Prediction.objects.all()
    return prediction
