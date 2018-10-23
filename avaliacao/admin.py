from django.contrib import admin

from avaliacao import models

@admin.register(models.Processo)
class ProcessoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Prova)
class ProvaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Criterio)
class CriterioAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    pass
