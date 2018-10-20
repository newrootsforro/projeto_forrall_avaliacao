from django.db import models


class Movimento(models.Model):
    nome = models.CharField(max_length=55)
    descricao = models.TextField()
