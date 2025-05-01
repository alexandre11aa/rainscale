from django.contrib import admin

from location.models import Nation, Region


class RegionInline(admin.TabularInline):
    """
    Exibe as Máquinas da Instituição.
    """
    fields = ('id', 'nome')
    model = Region
    extra = 0


@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ['nome']
    list_filter = ('id',)
    inlines = [RegionInline]


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nacao')
    search_fields = ['nome']
    list_filter = ('id',)