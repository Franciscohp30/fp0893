from django.conf import settings
from django.db import models


class Clientes(models.Model):
    Nome = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Clientes'

# Create your models here.
