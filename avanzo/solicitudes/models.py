from pyexpat import model
from django.db import models
from clientes.models import Cliente

class Solicitud(models.Model):
    monto = models.IntegerField()
    interes = models.FloatField()
    plazo = models.IntegerField()
    estado = models.BooleanField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default = None)

    def __str__(self):
        return '%s %s %s' % (self.cliente.pk, self.monto, self.estado)

