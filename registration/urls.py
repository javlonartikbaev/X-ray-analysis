from django.contrib import admin
from django.urls import path

from registration import views

urlpatterns = [
    path('client_list/', views.ClientListAPI.as_view(), name='client_list'),
    path('client_create/', views.ClientCreateAPI.as_view(), name='client_create'),
    path('client_delete/<int:client_id>/', views.ClientDeleteAPI.as_view(), name='client_delete'),
    path('client_update/<int:client_id>/', views.ClientUpdateAPI.as_view(), name='client_update'),
    path('client_detail/<int:client_id>/', views.ClientDetailAPI.as_view(), name='client_detail'),
]
