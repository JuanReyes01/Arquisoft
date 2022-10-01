from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core import serializers
import json

from .logic import archivo_logic as al

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

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        file_system_storage = FileSystemStorage()
        file_name = file_system_storage.save(uploaded_file.name, uploaded_file)
        url = file_system_storage.url(file_name)
        context['url'] = url

        json_archivo = {
            "nombre": uploaded_file.name,
            "archivo": url
        }

        archivo_dto = al.create_archivo(json_archivo)
        archivo = serializers.serialize('json', [archivo_dto,])

    return render(request, 'avanzo/base.html') # tiene que ser un render! por algo de seguridad de Django -> csrf_token
    # se pueden mandar variables al html! -> context

@csrf_exempt
def archivos_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id:
            archivo_dto = al.get_archivo(id)
            archivo = serializers.serialize('json', [archivo_dto,])
            return HttpResponse(archivo, 'application/json')
        else:
            archivos_dto = al.get_archivos()
            archivos = serializers.serialize('json', archivos_dto)
            return HttpResponse(archivos, 'application/json')

@csrf_exempt
def archivo_view(request, pk):
    if request.method == 'GET':
        archivo_dto = al.get_archivo(pk)
        archivo = serializers.serialize('json', [archivo_dto,])
        return HttpResponse(archivo, 'application/json')
    
    if request.method == 'PUT':
        archivo_dto = al.update_archivo(pk, json.loads(request.body))
        archivo = serializers.serialize('json', [archivo_dto,])
        return HttpResponse(archivo, 'application/json')
    
    if request.method == 'DELETE':
        al.delete_archivo(pk)
        return HttpResponse('Archivo eliminado', 'application/json')