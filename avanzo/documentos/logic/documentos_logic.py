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

def validar_documento(var_documento, var_criterios):
    if var_documento.salario < var_criterios.umbral:
        return False
    return True

def create_documento(var_documento):
    cliente = cliente.objects.get(pk=var_documento["cliente"])
    documento = Documento(
        nombre=var_documento["nombre"], 
        tipo=var_documento["tipo"], 
        fecha=var_documento["fecha"], 
        saldo=var_documento["saldo"], 
        cuentaBancaria=var_documento["cuentaBancaria"], 
        cliente=cliente)
    return documento