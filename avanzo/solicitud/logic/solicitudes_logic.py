from cliente.models import Cliente
from ..models import Solicitud

def get_solicitudes():
    solicitudes = Solicitud.objects.all()
    return solicitudes

def get_solicitud(sol_pk):
    solicitud = Solicitud.objects.get(pk=sol_pk)
    return solicitud

def update_solicitud(sol_pk, new_sol):
    solicitud = get_solicitud(sol_pk)
    solicitud.monto = new_sol["monto"]
    solicitud.interes = new_sol["interes"]
    solicitud.plazo = new_sol["plazo"]
    solicitud.estado = new_sol["estado"]
    solicitud.cliente = new_sol["cliente"]
    solicitud.save()
    return solicitud

def create_solicitud(sol):
    cliente = Cliente(
        cedula = sol["cedula"],
        nombre = sol["nombre"],
        telefono = sol["telefono"],
        correo = sol["correo"],
        direccion = sol["direccion"],
        password = sol["password"]
    )
    solicitud = Solicitud(
        monto = sol["monto"],
        interes = sol["interes"],
        plazo = sol["plazo"],
        estado = sol["estado"],
        cliente = cliente
    )
    solicitud.save()
    return solicitud

def delete_solicitud(sol_pk):
    solicitud = get_solicitud(sol_pk)
    solicitud.delete()
    return solicitud