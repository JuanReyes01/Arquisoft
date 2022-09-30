from django.shortcuts import render
from .logic import criterios_logic as dl
from django.http import HttpResponse
from django.core import serializers as serializers
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def criterios_view(request):
    if request.method == 'GET':
        id = request.GET.get('id',None)
        if id:
            criterio_dto=dl.get_criterio(id)
            criterio = serializers.serialize('json', criterio_dto)
            return HttpResponse(criterio, 'application/json')
        else:
            criterios_dto=dl.get_criterios()
            criterios = serializers.serialize('json', criterios_dto)
            return HttpResponse(criterios, 'application/json')
    elif request.method == 'POST':
        criterio_dto = json.loads(request.body)
        criterio = dl.create_criterio(criterio_dto)
        return HttpResponse(criterio, 'application/json')

@csrf_exempt
def criterio_view(request, pk):
    if request.method == 'GET':
        criterio_dto = dl.get_criterio(pk)
        criterio = serializers.serialize('json', [criterio_dto,])
        return HttpResponse(criterio, 'application/json')

    if request.method == 'PUT':
        criterio_dto = dl.update_criterio(pk, json.loads(request.body))
        criterio = serializers.serialize('json', [criterio_dto,])
        return HttpResponse(criterio, 'application/json')