from django.db import models
from cliente.models import Cliente
# Create your models here.
class Documento(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)
    fecha = models.DateField()
    saldo = models.FloatField()
    cuentaBancaria = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default = None)
    def __str__(self):
        return self.nombre