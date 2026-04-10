from django.contrib import admin
from .models import Espaco, Reserva


@admin.register(Espaco)
class EspacoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'capacidade', 'possui_computadores')
    list_filter = ('tipo', 'possui_computadores')
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'espaco', 'data', 'hora_inicio', 'hora_fim')
    list_filter = ('data', 'espaco__tipo')
    search_fields = ('usuario__username', 'espaco__nome')
    ordering = ('-data', 'hora_inicio')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('usuario', 'espaco', 'descricao')
        }),
        ('Data e Horário', {
            'fields': ('data', 'hora_inicio', 'hora_fim')
        }),
    )
