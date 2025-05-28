"""Configuración de la aplicación de usuarios.

Este módulo define la configuración básica de la aplicación de usuarios,
que incluye la configuración del modelo y el nombre de la aplicación.
"""

from django.apps import AppConfig


class UserConfig(AppConfig):
    """Configuración de la aplicación de usuarios.

    Esta clase configura la aplicación de usuarios, especificando el tipo
    de campo autoincremental y el nombre de la aplicación.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "user"
