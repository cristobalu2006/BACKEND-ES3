from django.db import models

class Autor(models.Model):
    nombre = models.CharField(null=False, max_length=200)
    nacionalidad = models.CharField(null=False, max_length=200)
    anio_nacimiento = models.PositiveIntegerField(null=False, max_length=3)