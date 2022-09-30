from ..models import Documento

def get_documentos():
    return Documento.objects.all()

def get_documento(var_pk):
    return Documento.objects.get(pk=var_pk)

def update_documento(var_pk, var_documento):
    documento = Documento.objects.get(pk=var_pk)
    documento.salario = var_documento.salario
    documento.cuentaBancaria = var_documento.cuentaBancaria
    documento.save()
    return documento