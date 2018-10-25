from django.db import models
from django.contrib.auth.models import User

from cadastro.models import Nivel, Aluno, Processo


class Movimento(models.Model):
    nome = models.CharField(max_length=55)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Criterio(models.Model):
    nome = models.CharField(max_length=55)
    descricao = models.CharField(max_length=255)
    pontuacao_reprovacao = models.IntegerField()
    pontuacao_aprovacao = models.IntegerField()

    def __str__(self):
        return self.nome


class Prova(models.Model):
    titulo  = models.CharField(max_length=55)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    criterios = models.ManyToManyField(Criterio)

    def __str__(self):
        return self.titulo


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

    def __str__(self):
        return f'{self.criterio.nome} - {self.prova.titulo} - {self.avaliado.nome}'
