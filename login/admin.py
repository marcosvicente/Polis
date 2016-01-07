from django.contrib import admin

from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_fields = ('nome')

admin.site.register(Usuario ,UsuarioAdmin)
