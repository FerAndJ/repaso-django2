from django.db import models

# Create your models here.

class Cerrajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    desempleado = models.BooleanField()
    
class Futbolista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    desempleado = models.BooleanField()   
    club_ftubol = models.CharField(max_length=50)