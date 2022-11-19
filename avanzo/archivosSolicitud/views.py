import time
from random import randint
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core import serializers
import json
from .models import ArchivoSolicitud
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
def upload(request):
    f = open('docs/logs.txt', 'a')
    if request.method == 'POST':
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
    # se pueden mandar variables a html! -> context

def archivos_view(request):
    archivos_list = ArchivoSolicitud.objects.all()
    archivo_pk = None
    return render(
                  request,
                  'avanzo/file_selection.html',
                  {'archivos_list': archivos_list}
                 )

@csrf_exempt
def archivo_view(request, pk):
    f = open('docs/logs.txt', 'a')
    post = get_object_or_404(ArchivoSolicitud, id=request.POST.get('post_id'))

    f.write("GET request to MODIFY FILE - 'archivoSolicitud' - ID Object: " + str(post.pk) + "\n")
    f.close()
    return HttpResponse(post, 'application/json')
    
@csrf_exempt
def updateDelete_view(request, pk):
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