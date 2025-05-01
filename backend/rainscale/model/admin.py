from django.contrib import admin

from model.models import Model


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'regiao', 'autor')
    search_fields = ('id', 'nome')
    list_filter = ('id', 'regiao', 'autor',)