from django.contrib import admin
from django.urls import path
from . import views

urlspatterns = [
    path('', views.solicitudes_view, name='solicitudes_view'),
    path('<int:pk>', views.solicitud_view, name='solicitud_view'),
]