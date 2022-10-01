from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes_view, name='clientes'),
    path('<int:pk>', views.cliente_view, name='cliente'),
]