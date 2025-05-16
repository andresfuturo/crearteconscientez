# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import CustomUser, ProgresoUsuario

#se crea como un diccionario {clave : llave} guarda un registro de esa manera
@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ('username', 'password')}),
        ('Personal Information', {
            "fields": (
                'first_name', 'last_name', 'email',
                'nombre', 'apellido', 'fecha_nacimiento'
            )
        }),
        ('Permissions', {"fields": ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {"fields": ('last_login', 'date_joined')}),
    )
#guarda el progreso del usuario la eleccion del avatar
@admin.register(ProgresoUsuario)
class ProgresoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'mision_iniciada', 'mision_inicio_fecha')
    search_fields = ('user__username', 'avatar')
    list_filter = ('avatar', 'mision_iniciada')
