from django.db import models
from django.contrib.auth.models import User

from alunos.models import Nivel, Aluno


class Movimento(models.Model):
    nome = models.CharField(max_length=55)
    descricao = models.TextField()



class Criterio(models.Model):
    nome = models.CharField(max_length=55)
    descricao = models.CharField(max_length=255)
    pontuacao_reprovacao = models.IntegerField()
    pontuacao_aprovacao = models.IntegerField()


class Prova(models.Model):
    titulo  = models.CharField(max_length=55)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    criterios = models.ManyToManyField(Criterio)


class Avaliacao(models.Model):
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE)
    criterio = models.ForeignKey(Criterio, on_delete=models.CASCADE)
    avaliado = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    avaliador = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=55,
        choices= (
            ('a', 'Aprovado'), 
            ('r', 'Reprovado'),
        )
    )

    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliações'