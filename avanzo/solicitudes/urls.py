from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.solicitudes_view, name='solicitudes'),
    path('<int:pk>', views.solicitud_view, name='solicitud'),
]