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

MESES = (
    ('Jan', 'Janeiro'),
    ('Fev', 'Fevereiro'),
    ('Mar', 'Março'),
    ('Abr', 'Abril'),
    ('Maio', 'Maio'),
    ('Jun', 'Junho'),
    ('Jul', 'Julho'),
    ('Ago', 'Agosto'),
    ('Set', 'Setembro'),
    ('Out', 'Outubro'),
    ('Nov', 'Novembro'),
    ('Dez', 'Dezembro'),
)

class Aluno(models.Model):

    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email=models.CharField(max_length=255,blank=True,null=True)
    nivel=models.CharField(choices=ALUNOS_NIVEIS, max_length=55)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return "Aluno[{}={}]".format(self.nome, self.nivel)


class Pagamentos(models.Model):

    aluno = models.ForeignKey(
        'Aluno',
        on_delete=models.CASCADE,
    )

    mes=models.CharField(choices=MESES, max_length=55)
    valor = models.IntegerField(default=50)
    data_pagamento = models.DateField(blank=True,null=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    observacao = models.TextField()


    def __str__(self):
        return '{} - {}'.format(
            self.aluno.nome,
            self.mes
        )
