from sys import maxsize
from django.db import models

# Create your models here.
# 2do commit
class Persona(models.Model):
    nombre = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    edad = models.IntegerField()
    donador = models.BooleanField()
    utilizarNull = models.BooleanField(default=False)
    utilizarNull2 = models.BooleanField(null=True)
    utilizarBlank = models.BooleanField(blank=True)