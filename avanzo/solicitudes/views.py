from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core import serializers
import json

from .logic import solicitudes_logic as st

# Create your views here.

@csrf_exempt
def solicitudes_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id:
            solicitud_dto = st.get_solicitud(id)
            solicitud = serializers.serialize('json', [solicitud_dto,])
            return HttpResponse(solicitud, 'application/json')
        else:
            solicitudes_dto = st.get_solicitudes()
            solicitudes = serializers.serialize('json', solicitudes_dto)
            return HttpResponse(solicitudes, 'application/json')

@csrf_exempt
def solicitud_view(request, pk):
    if request.method == 'GET':
        solicitud_dto = st.get_solicitud(pk)
        solicitud = serializers.serialize('json', [solicitud_dto,])
        return HttpResponse(solicitud, 'application/json')
    
    if request.method == 'PUT':
        solicitud_dto = st.update_solicitud(pk, json.loads(request.body))
        solicitud = serializers.serialize('json', [solicitud_dto,])
        return HttpResponse(solicitud, 'application/json')

    if request.method == 'DELETE':
        st.delete_solicitud(pk)
        return HttpResponse('Solicitud eliminada', 'application/json')
    
    
    
    
