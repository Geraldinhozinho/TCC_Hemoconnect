from django.contrib import admin
from .models import Usuario, Questionario, Campanhas, Doacoes, Criador, ChatFAQ
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Questionario)
admin.site.register(Campanhas)
admin.site.register(Doacoes)
admin.site.register(Criador)

# Inline para Doacoes
class DoacoesInline(admin.TabularInline):  # Inline no formato de tabela
    model = Doacoes  # Relacionado ao modelo Doacoes
    extra = 1  # Número de linhas extras para adicionar novas doações
    fields = ('data_doacao', 'data_prox_doacao')  # Campos a serem exibidos

# Customização do UsuarioAdmin
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('endereco', 'cpf', 'nome_completo', 'foto_perfil')}),
    )
    inlines = [DoacoesInline]  # Vincula as doações ao usuário

@admin.register(ChatFAQ)
class ChatFAQAdmin(admin.ModelAdmin):
    list_display = ('pergunta',)
    search_fields = ('pergunta', 'resposta')

# Registro do Usuario com o UsuarioAdmin personalizado
admin.site.register(Usuario, UsuarioAdmin)