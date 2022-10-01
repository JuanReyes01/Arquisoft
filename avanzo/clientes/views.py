from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core import serializers
import json

from .logic import clientes_logic as st

# Create your views here.

@csrf_exempt
def clientes_view(request):
    if request.method == 'GET':
        Id = request.GET.get('Id', None)
        if Id:
            cliente_dto = st.get_cliente(Id)
            cliente = serializers.serialize('json', [cliente_dto,])
            return HttpResponse(cliente, 'application/json')
        else:
            clientes_dto = st.get_clientes()
            clientes = serializers.serialize('json', clientes_dto)
            return HttpResponse(clientes, 'application/json')
    elif request.method == 'POST':
        cliente_dto = json.loads(request.body)
        cliente = st.create_cliente(cliente_dto)
        return HttpResponse(cliente, 'application/json')

    return render(request, 'avanzo/base.html', context) # tiene que ser un render! por algo de segurIdad de Django -> csrf_token
    # se pueden mandar variables al html! -> context

@csrf_exempt
def cliente_view(request, pk):
    if request.method == 'GET':
        cliente_dto = st.get_cliente(pk)
        cliente = serializers.serialize('json', [cliente_dto,])
        return HttpResponse(cliente, 'application/json')
    
    if request.method == 'PUT':
        cliente_dto = st.update_cliente(pk, json.loads(request.body))
        cliente = serializers.serialize('json', [cliente_dto,])
        return HttpResponse(cliente, 'application/json')

    if request.method == 'DELETE':
        st.delete_cliente(pk)
        return HttpResponse('Cliente eliminado', 'application/json')
