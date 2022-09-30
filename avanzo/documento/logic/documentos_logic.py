from ..models import Documento

def get_documentos():
    return Documento.objects.all()

