from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core import serializers
import json

from .logic import solicitudes_logic as st
from django.contrib.auth.decorators import login_required
from avanzo.auth0backend import getRole

# Create your views here.

@csrf_exempt
def solicitudes_view(request):
    role = getRole(request)
    if request.method == 'GET' and role == "analista":
        id = request.GET.get('id', None)
        if id:
            solicitud_dto = st.get_solicitud(id)
            solicitud = serializers.serialize('json', [solicitud_dto,])
            return HttpResponse(solicitud, 'application/json')
        else:
            solicitudes_dto = st.get_solicitudes()
            solicitudes = serializers.serialize('json', solicitudes_dto)
            return HttpResponse(solicitudes, 'application/json')

    context = {}
    if request.method == 'POST' and role == "analista":
        uploaded_file = request.FILES['document']
        file_system_storage = FileSystemStorage()
        file_name = file_system_storage.save(uploaded_file.name, uploaded_file)
        context['url'] = file_system_storage.url(file_name)

    return render(request, 'avanzo/base.html', context) # tiene que ser un render! por algo de seguridad de Django -> csrf_token
    # se pueden mandar variables al html! -> context

@csrf_exempt
def solicitud_view(request, pk):
    
    role = getRole(request)
    
    if request.method == 'GET' and role == "analista":
        solicitud_dto = st.get_solicitud(pk)
        solicitud = serializers.serialize('json', [solicitud_dto,])
        return HttpResponse(solicitud, 'application/json')
    
    if request.method == 'PUT' and role == "analista":
        solicitud_dto = st.update_solicitud(pk, json.loads(request.body))
        solicitud = serializers.serialize('json', [solicitud_dto,])
        return HttpResponse(solicitud, 'application/json')

    if request.method == 'DELETE' and role == "analista":
        st.delete_solicitud(pk)
        return HttpResponse('Solicitud eliminada', 'application/json')
    
    
    
    
