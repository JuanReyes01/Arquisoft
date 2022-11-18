from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.archivos_view, name='archivos'),
    path('', views.upload, name='upload'),
    path('<str:url>', views.archivo_view, name='archivo'),
]