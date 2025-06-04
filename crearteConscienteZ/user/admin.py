"""Administración de la aplicación de usuarios.

Este módulo define las interfaces de administración para los modelos de usuario
y progreso del usuario en el panel de administración de Django.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import CustomUser, ProgresoUsuario


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    """Administrador personalizado para usuarios.

    Esta clase extiende UserAdmin de Django para incluir campos
    adicionales como nombre, apellido y fecha de nacimiento.
    """

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Information", {
            "fields": (
                "first_name", "last_name", "email",
                "nombre", "apellido", "fecha_nacimiento",
            ),
        }),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


@admin.register(ProgresoUsuario)
class ProgresoUsuarioAdmin(admin.ModelAdmin):
    """Administrador para el progreso del usuario.

    Esta clase permite gestionar el progreso y la elección de avatar
    de los usuarios en el panel de administración.
    """

    list_display = ("user", "avatar", "mision_iniciada", "mision_inicio_fecha")
    search_fields = ("user__username", "avatar")
    list_filter = ("avatar", "mision_iniciada")
