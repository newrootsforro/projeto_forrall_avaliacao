# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


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


class Processo(models.Model):
    nome = models.CharField(max_length=55)
    data_realizacao = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return "Processo[{}={}]".format(self.nome, self.data_realizacao)


class Nivel(models.Model):

    nome = models.CharField(max_length=55)
    pontuacao_minima = models.IntegerField(blank=True,null=True)
    ordem = models.IntegerField(default=1)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return "Nivel[{}={}]".format(self.nome, self.ordem)


class Aluno(models.Model):

    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email=models.CharField(max_length=255,blank=True,null=True)
    nivel=models.ForeignKey(Nivel, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return "Aluno[{}={}]".format(self.nome, self.nivel)


class Avaliador(models.Model):
    nome = models.CharField(max_length=255)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


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
