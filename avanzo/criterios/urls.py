from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.criterios_view, name='criterios_view'),
    path('<int:var_pk>', views.criterio_view, name='criterio_view'),
    ]