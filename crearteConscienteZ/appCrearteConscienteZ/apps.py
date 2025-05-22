"""Configuración de la aplicación Crearte ConscienteZ.

Este módulo contiene la configuración básica de la aplicación, incluyendo:
- Configuración de campos automáticos
- Nombre de la aplicación
"""

from django.apps import AppConfig


class AppcrearteconscientezConfig(AppConfig):
    """Configuración específica de la aplicación Crearte ConscienteZ."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "appCrearteConscienteZ"
