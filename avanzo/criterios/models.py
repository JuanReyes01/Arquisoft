from django.db import models
from documentos.models import Documento

# Create your models here.
class Criterio(models.Model):
    nombre = models.CharField(max_length=100)
    umbral = models.FloatField(null = True, blank = True)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE) #(Documento, null = True, blank = True)
    def __str__(self):
        return self.nombre
