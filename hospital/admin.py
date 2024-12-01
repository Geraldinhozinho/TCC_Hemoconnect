from django.contrib import admin
from .models import Usuario, Questionario, Campanhas, Doacoes, Criador, ChatFAQ
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Questionario)
admin.site.register(Campanhas)
admin.site.register(Doacoes)
admin.site.register(Criador)

class DoacoesInline(admin.TabularInline):  
    model = Doacoes 
    extra = 1  
    fields = ('data_doacao', 'data_prox_doacao')  
# Customização do UsuarioAdmin
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('endereco', 'cpf', 'nome_completo', 'foto_perfil')}),
    )
    inlines = [DoacoesInline]  
@admin.register(ChatFAQ)
class ChatFAQAdmin(admin.ModelAdmin):
    list_display = ('pergunta',)
    search_fields = ('pergunta', 'resposta')
# Registro do Usuario com o UsuarioAdmin personalizado
admin.site.register(Usuario, UsuarioAdmin)