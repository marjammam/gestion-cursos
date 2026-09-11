from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Docente, Estudiante


class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Tipo de usuario', {'fields': ('tipo_usuario',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Tipo de usuario', {'fields': ('tipo_usuario',)}),
    )


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Docente)
admin.site.register(Estudiante)