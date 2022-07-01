from sys import maxsize
from django.db import models
from django.urls import reverse

# Create your models here.
# 2do commit
class Persona(models.Model):
    nombre = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    edad = models.IntegerField(blank= True)
    donador = models.BooleanField()

    def get_absolute_url(self):
        return reverse('auxiliar:browsing', kwargs={'myID': self.id})
    