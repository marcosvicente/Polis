from django.db import models


class Cadrastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    usuario = models.CharField(max_length=100)
    dia = models.IntegerField()
    mes = models.CharField(max_length=100)
    ano = models.IntegerField()
    senha = models.CharField(max_length=100) 



