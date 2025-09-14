from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import CustomUser


# class ModelInline(admin.TabularInline):
#     """
#     Exibe os Modelos do Usuário.
#     """
#     model = CustomUser.modelo.through
#     extra = 1


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    
    # Campos exibidos na lista de usuários
    list_display = (
        'id', 'email', 'nome', 'is_staff'
    )
    
    # Campos utilizados para pesquisa no painel administrativo
    search_fields = ('email',)
    
    # Filtros disponíveis para filtrar usuários na lista
    list_filter = ('is_staff', 'is_active')
    
    # Ordem de exibição dos usuários na lista
    ordering = ('nome',)
    
    # Configurações para os formulários de edição e visualização
    fieldsets = (
        # Seção principal com campos básicos
        (None, {'fields': ('code', 'email', 'nome', 'password')}),
                
        # Seção de permissões
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    
    # Campos a serem exibidos ao adicionar um novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'password1', 'password2', 'is_staff', 'is_superuser')
        }),
    )

    # inlines = [ModelInline]
    
    filter_horizontal = ()