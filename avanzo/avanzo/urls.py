"""avanzo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from archivosSolicitud import views
from avanzo import views as vw

urlpatterns = [
    path('', vw.index),
    #path('', include('archivosSolicitud.urls')),
    #path('home/',  views.home),
    #path('documentos/', include('documentos.urls')),
    #path('upload/', views.upload),
    #path('archivo/', include('archivosSolicitud.urls')),
    #path('solicitudes/', include('solicitudes.urls')),
    #path('criterios/', include('criterios.urls')),
    #path('clientes/', include('clientes.urls')),
]

