from django.db import models
from django.auth.models import User

from alunos.models import Nivel, Aluno


class Movimento(models.Model):
    nome = models.CharField(max_length=55)
    descricao = models.TextField()


class Processo(models.Model):
    nome = models.CharField(max_length=55)
    data_realizacao = models.DateField(blank=True, null=True)


class Criterio(models.Model):
    nome = models.CharField(max_length=55)
    descricao = models.CharField(max_length=255)
    pontuacao_reprovacao = models.IntegerField()
    pontuacao_aprovacao = models.IntegerField()


class Prova(models.Model):
    titulo  = models.CharField(max_length=55)
    nivel = models.ForeignKey(Nivel)
    processo = models.Foreign(Processo)
    criterios = models.ManyToManyField(Criterio)


class Avaliacao(models.Model):
    prova = models.ForeignKey(Prova)
    criterio = models.ForeignKey(Criterio)
    avaliado = models.Foreignkey(Aluno)
    avaliador = models.ForeignKey(User)
    status = models.CharField(
        max_length=55,
        choices= (
            ('a', 'Aprovado'), 
            ('r', 'Reprovado'),
        )
    )

    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliações