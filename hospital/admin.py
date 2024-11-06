from django.contrib import admin
from .models import Usuario, Questionario, Campanhas
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Questionario)
admin.site.register(Campanhas)


class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('endereco','cpf')}),
    )

admin.site.register(Usuario, UsuarioAdmin)