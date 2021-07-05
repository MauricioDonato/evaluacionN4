from django.db import models
from django.db.models.base import Model
# Create your models here.
class Comuna(models.Model):
    nombre_c = models.CharField(max_length=20)

class Cliente(models.Model):
    rut =  models.CharField(max_length=13)
    nombre_cli = models.CharField(max_length=50,default='')
    apellido_cli = models.CharField(max_length=50,default='')
    fecha_nac = models.DateTimeField('Fecha de nacimiento del cliente')
    correo = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    contrasena_val = models.CharField(max_length=50)
    def __str__(self):
        return self.rut
