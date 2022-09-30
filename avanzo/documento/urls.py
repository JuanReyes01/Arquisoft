from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.documentos_view, name='documentos_view'),
    path('<int:var_pk>', views.documento_view, name='documento_view'),
    ]