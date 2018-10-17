# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


ALUNOS_NIVEIS = (
    ('branco', 'Branco'),
    ('amarelo', 'Amarelo'),
    ('laranja', 'Laranja'),
    ('verde', 'Verde'),
    ('azul claro', 'Azul Claro'),
)

class Aluno(models.Model):

    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email=models.CharField(max_length=255,blank=True,null=True)
    nivel=models.CharField(choices=ALUNOS_NIVEIS, max_length=55)
