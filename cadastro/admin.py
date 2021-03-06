# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    Aluno,
    Pagamentos,
    Nivel,
    Processo
)

@admin.register(Processo)
class ProcessoAdmin(admin.ModelAdmin):
    pass

class PagamentosInline(admin.StackedInline):
    model = Pagamentos

@admin.register(Aluno)
class AlunosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel',)
    inlines = [PagamentosInline,]


@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = ('nome',)

