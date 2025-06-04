"""Módulo de URLs para la aplicación de usuarios.

Este módulo define las rutas URL para las vistas de usuario,
principalmente la vista de registro de nuevos usuarios.

URLs:
    - /registro/: Vista de registro de usuarios
"""

from django.urls import path

from . import views

urlpatterns = [
    path("registro/", views.registro, name="registro"),
]
