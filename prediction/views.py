from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import serializers, status

from doctors.models import Doctor
from registration.models import Client
from .services import create_prediction, get_prediction


# Create your views here.
class CreatePredictionAPI(APIView):
    class InputSerializer(serializers.Serializer):
        client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
        img = serializers.ImageField(required=True)
        doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    class OutputSerializer(serializers.Serializer):
        client = serializers.CharField()
        img = serializers.ImageField()
        doctor = serializers.CharField()
        prediction = serializers.CharField()
        date = serializers.DateField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        prediction = create_prediction(**serializer.validated_data)
        data = self.OutputSerializer(prediction).data
        return Response(data, status=status.HTTP_201_CREATED)


class PredictionListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        client = serializers.CharField()
        img = serializers.ImageField()
        doctor = serializers.CharField()
        prediction = serializers.CharField()
        date = serializers.DateField()

    def get(self, request):
        predictions = get_prediction()
        data = self.OutputSerializer(predictions, many=True).data
        return Response(data, status=status.HTTP_200_OK)
