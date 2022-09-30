from django.shortcuts import HttpResponse, render
from .logic import documentos_logic as dl
# Create your views here.
def documentos_view(request):
    if request.method == 'GET':
        documentos = dl.get_documentos()
        documentos_dto = serializers.serialize('json', documentos)
        return HttpResponse(documentos_dto, 'application/json')