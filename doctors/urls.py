from django.contrib import admin
from django.urls import path

from doctors import views

urlpatterns = [
    path('list/', views.DoctorListAPI.as_view(), name='client_list'),
    path('create/', views.DoctorCreateAPI.as_view(), name='doctor_create'),
    # path('client_delete/<int:client_id>/', views.ClientDeleteAPI.as_view(), name='client_delete'),
    # path('client_update/<int:client_id>/', views.ClientUpdateAPI.as_view(), name='client_update'),
    # path('client_detail/<int:client_id>/', views.ClientDetailAPI.as_view(), name='client_detail'),
]
