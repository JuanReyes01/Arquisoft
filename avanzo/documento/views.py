from .logic import documentos_logic as dl
from django.http import HttpResponse
from django.core import serializers as serializers
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def documentos_view(request):
    if request.method == 'GET':
        id = request.GET.get('id',None)
        if id:
            documento_dto=dl.get_documento(id)
            documento = serializers.serialize('json', documento_dto)
            return HttpResponse(documento, 'application/json')
        else:
            documentos_dto=dl.get_documentos()
            documentos = serializers.serialize('json', documentos_dto)
            return HttpResponse(documentos, 'application/json')
    elif request.method == 'POST':
        documento_dto = json.loads(request.body)
        documento = dl.create_documento(documento_dto)
        return HttpResponse(documento, 'application/json')

@csrf_exempt
def documento_view(request, pk):
    if request.method == 'GET':
        documento_dto = dl.get_documento(pk)
        documento = serializers.serialize('json', [documento_dto,])
        return HttpResponse(documento, 'application/json')

    if request.method == 'PUT':
        documento_dto = dl.update_documento(pk, json.loads(request.body))
        documento = serializers.serialize('json', [documento_dto,])
        return HttpResponse(documento, 'application/json')

