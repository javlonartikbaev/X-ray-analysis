from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import serializers, status
from config.serializers import inline_serializer
from .models import Doctor
from .services import create_doctor


class DoctorCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        full_name = serializers.CharField()
        phone_number = serializers.CharField(max_length=14)
        password = serializers.CharField(max_length=12)
        img = serializers.ImageField(required=False)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        full_name = serializers.CharField()
        phone_number = serializers.CharField(max_length=14)
        password = serializers.CharField(max_length=12)
        img = serializers.ImageField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doctor = create_doctor(**serializer.validated_data)
        data = self.OutputSerializer(doctor).data
        return Response(data, status=status.HTTP_201_CREATED)


class DoctorListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        full_name = serializers.CharField()
        phone_number = serializers.CharField(max_length=14)
        password = serializers.CharField(max_length=12)
        img = serializers.ImageField()

    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = self.OutputSerializer(doctors, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
