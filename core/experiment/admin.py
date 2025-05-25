from django.contrib import admin

from experiment.models import Simulation, LocalData


@admin.register(Simulation)
class SimulationAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ['nome']
    list_filter = ('id',)


@admin.register(LocalData)
class LocalDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ['nome']
    list_filter = ('id',)