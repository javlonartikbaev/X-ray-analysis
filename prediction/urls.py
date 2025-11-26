from django.contrib import admin
from django.urls import path

from doctors import views
from .views import CreatePredictionAPI, PredictionListAPI

urlpatterns = [

    path('predict/', CreatePredictionAPI.as_view(), name='prediction'),
    path('list/', PredictionListAPI.as_view(), name='prediction'),
    # path('client_delete/<int:client_id>/', views.ClientDeleteAPI.as_view(), name='client_delete'),
    # path('client_update/<int:client_id>/', views.ClientUpdateAPI.as_view(), name='client_update'),
    # path('client_detail/<int:client_id>/', views.ClientDetailAPI.as_view(), name='client_detail'),
]
