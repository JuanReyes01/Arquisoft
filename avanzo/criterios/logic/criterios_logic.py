from ..models import Criterio

def get_criterios():
    return Criterio.objects.all()

def get_criterio(var_pk):
    return Criterio.objects.get(pk=var_pk)

def update_criterio(var_pk, var_criterio):
    criterio = Criterio.objects.get(pk=var_pk)
    criterio.nombre = var_criterio.nombre
    criterio.umbral = var_criterio.umbral
    criterio.save()
    return criterio