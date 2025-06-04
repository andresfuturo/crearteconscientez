"""Modelos de la aplicación Crearte ConscienteZ.

Este módulo contiene los modelos de datos principales de la aplicación, incluyendo:
- Avatar: Modelo para representar a los avatares de los usuarios
"""

from django.db import models


class Avatar(models.Model):
    """Modelo que representa un avatar en la aplicación.

    Atributos:
        nombre: Nombre del avatar
        nivel: Nivel actual del avatar
        fuego: Indica si el avatar tiene la habilidad de fuego
        agua: Indica si el avatar tiene la habilidad de agua
        tierra: Indica si el avatar tiene la habilidad de tierra
        aire: Indica si el avatar tiene la habilidad de aire
    """
    nombre = models.CharField(max_length=100)
    nivel = models.IntegerField(default=1)
    fuego = models.BooleanField(default=False)
    agua = models.BooleanField(default=False)
    tierra = models.BooleanField(default=False)
    aire = models.BooleanField(default=False)
    # Puedes agregar otros atributos como experiencia, poderes, etc.

    class Meta:
        """Metadatos de la tabla Avatar.

        Personaliza el nombre de la tabla en la base de datos para mejor organización.
        """
        db_table = "appcrearteconscientez_avatar"  # Personalizando el nombre de la tabla de avatares

    def __str__(self) -> str:
        """Devuelve el nombre del avatar como representación string."""
        return self.nombre
