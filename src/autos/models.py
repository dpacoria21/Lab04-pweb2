from django.db import models

# Create your models here.
# 1er commit
class Auto(models.Model):
    marca = models.TextField()
    placa = models.CharField(max_length=8)
    tiempoUso = models.IntegerField()