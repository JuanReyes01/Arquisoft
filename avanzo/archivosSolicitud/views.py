import time
from random import randint
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core import serializers
import json
from documentos.models import Documento
from .logic import archivo_logic as al
import logging
logger = logging.getLogger(__name__)

# Create your views here.

# def upload(request):
#     context = {}
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         file_system_storage = FileSystemStorage()
#         file_name = file_system_storage.save(uploaded_file.name, uploaded_file)
#         context['url'] = file_system_storage.url(file_name)

#     return render(request, 'avanzo/base.html') # tiene que ser un render! por algo de seguridad de Django -> csrf_token
#     # se pueden mandar variables al html! -> context

context = {}

def home(request):
    return render(request, 'avanzo/loginpage.html')

def upload(request):
    f = open('docs/logs.txt', 'a')
    if request.method == 'POST':
        # documento = Documento(
        # nombre="", 
        # #tipo="", 
        # #fecha=None, 
        # #saldo=0, 
        # #cuentaBancaria=0, 
        # #cliente=None
        # )
        uploaded_file = request.FILES['document']
        #uploaded_file = request.POST.get('document', documento)
        file_system_storage = FileSystemStorage()
        file_name = file_system_storage.save(uploaded_file.name, uploaded_file)
        url = file_system_storage.url(file_name)
        context[file_name] = url

        json_archivo = {
            "nombre": uploaded_file.name,
            "archivo": url
        }
        #t = randint(150,180)
        #time.sleep(t)
        archivo_dto = al.create_archivo(json_archivo)
        archivo = serializers.serialize('json', [archivo_dto,])
        f.write("POST request - 'archivoSolicitud' - File: " + uploaded_file.name + " - Path: " + url + "\n")
        f.close()
        

    return render(request, 'avanzo/base.html') # tiene que ser un render! por algo de seguridad de Django -> csrf_token
    # se pueden mandar variables al html! -> context

@csrf_exempt
def archivos_view(request):
    f = open('docs/logs.txt', 'a')
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id:
            archivo_dto = al.get_archivo(id)
            archivo = serializers.serialize('json', [archivo_dto,])
            f.write("GET request - 'archivoSolicitud'\n")
            f.close()
            return HttpResponse(archivo, 'application/json')
        else:
            archivos_dto = al.get_archivos()
            archivos = serializers.serialize('json', archivos_dto)
            f.write("GET request - 'archivoSolicitud'\n")
            f.close()
            return HttpResponse(archivos, 'application/json')

@csrf_exempt
def archivo_view(request, url):
    print(url)
    f = open('docs/logs.txt', 'a')
    # requested_file = request.FILES['url']
    # file_system_storage = FileSystemStorage()
    # file_name = file_system_storage.save(requested_file.name, requested_file)
    # off_name = None
    # off_url = None
        
    archivo = {
        "nombre": "stumpy",
        "archivo": "www"
    }
    #archivo_dto = al.get_archivo(pk)
    #archivo = serializers.serialize('json', [archivo_dto,])
    #f.write("GET request - 'archivoSolicitud' - ID Object: " + off_name + "\n")
    #f.close()
    return HttpResponse(archivo, 'application/json')
    
    if request.method == 'PUT':
        archivo_dto = al.update_archivo(pk, json.loads(request.body))
        archivo = serializers.serialize('json', [archivo_dto,])
        f.write("PUT request - 'archivoSolicitud' - ID Object: " + str(pk) + "\n")
        f.close()
        return HttpResponse(archivo, 'application/json')
    
    if request.method == 'DELETE':
        al.delete_archivo(pk)
        f.write("DELETE request - 'archivoSolicitud' - ID Object: " + str(pk) + "\n")
        f.close()
        return HttpResponse('Archivo eliminado', 'application/json')