"""Módulo de modelos para la aplicación de usuarios.

Este módulo define los modelos de datos para la gestión de usuarios y su progreso,
incluyendo información personal y el estado de las misiones.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Modelo personalizado de usuario que extiende AbstractUser.

    Agrega campos adicionales para información personal del usuario.

    Atributos:
        nombre: Nombre del usuario
        apellido: Apellido del usuario
        fecha_nacimiento: Fecha de nacimiento del usuario (opcional)
    """

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(null=True, blank=True)


#progreso del usuario escoge un elemento
class ProgresoUsuario(models.Model):
    """Modelo que representa el progreso del usuario en la aplicación.

    Este modelo mantiene el estado de las misiones y el avatar seleccionado
    por el usuario.

    Atributos:
        user: Relación uno a uno con el modelo CustomUser
        avatar: Avatar seleccionado por el usuario
        mision_iniciada: Indica si el usuario ha iniciado su misión
        mision_inicio_fecha: Fecha de inicio de la misión (opcional)
    """

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=30, choices=[
        ("aire_femenina", "Aire Femenina"),
        ("fuego_femenina", "Fuego Femenina"),
        ("agua_femenina", "Agua Femenina"),
        ("tierra_femenina", "Tierra Femenina"),

    ])
    mision_iniciada = models.BooleanField(default=False)
    mision_inicio_fecha = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        """Devuelve una representación legible del progreso del usuario.

        Returns:
            str: Cadena que muestra el nombre de usuario, avatar y estado de la misión

        """
        return f"{self.user.username} - {self.avatar} - {'Iniciada' if self.mision_iniciada else 'No iniciada'}"

