from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.serializers import inline_serializer
from .selectors import get_client, get_clients
from .services import create_client, update_client, delete_client
from .models import Client


class ClientListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        full_name = serializers.CharField()
        phone_number = serializers.CharField()
        passport_seria = serializers.CharField()
        passport_pinfl = serializers.CharField()
        date_of_birth = serializers.DateField()
        gender = serializers.CharField()

    class ClientFilterSerializer(serializers.Serializer):
        full_name = serializers.CharField(required=False)
        passport_seria = serializers.CharField(required=False)
        passport_pinfl = serializers.CharField(required=False)
        gender = serializers.ChoiceField(required=False, choices=Client.Gender.choices)

    def get(self, request):
        filter_serializer = self.ClientFilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)
        clients = get_clients(filters=filter_serializer.validated_data)
        data = self.OutputSerializer(clients, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class ClientCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        full_name = serializers.CharField()
        phone_number = serializers.CharField()
        passport_seria = serializers.CharField()
        passport_pinfl = serializers.CharField()
        date_of_birth = serializers.DateField()
        gender = serializers.ChoiceField(choices=Client.Gender.choices)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        full_name = serializers.CharField()
        phone_number = serializers.CharField()
        passport_seria = serializers.CharField()
        passport_pinfl = serializers.CharField()
        date_of_birth = serializers.DateField()
        gender = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = create_client(**serializer.validated_data)
        return Response(self.OutputSerializer(client).data, status=status.HTTP_201_CREATED)


class ClientDeleteAPI(APIView):
    def delete(self, request, client_id):
        delete_client(client_id=client_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientUpdateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        phone_number = serializers.CharField(required=False)
        passport_seria = serializers.CharField(required=False)
        passport_pinfl = serializers.CharField(required=False)
        date_of_birth = serializers.DateField(required=False)
        gender = serializers.ChoiceField(choices=Client.Gender.choices, required=False)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        full_name = serializers.CharField()
        phone_number = serializers.CharField()
        passport_seria = serializers.CharField()
        passport_pinfl = serializers.CharField()
        date_of_birth = serializers.DateField()
        gender = serializers.CharField()

    def put(self, request, client_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = update_client(client_id=client_id, **serializer.validated_data)
        return Response(self.OutputSerializer(client).data, status=status.HTTP_200_OK)


class ClientDetailAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        full_name = serializers.CharField()
        phone_number = serializers.CharField()
        passport_seria = serializers.CharField()
        passport_pinfl = serializers.CharField()
        date_of_birth = serializers.DateField()
        gender = serializers.CharField()

    def get(self, request, client_id):
        client = get_client(client_id=client_id)
        data = self.OutputSerializer(client).data
        return Response(data, status=status.HTTP_200_OK)
