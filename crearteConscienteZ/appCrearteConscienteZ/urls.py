"""Módulo de URLs de la aplicación Crearte ConscienteZ.

Este módulo define las rutas URL de la aplicación, incluyendo:
- Rutas principales de la aplicación
- Configuración de URLs estáticas para archivos multimedia
- Rutas de autenticación y registro
"""

from django.conf import settings  # type: ignore[import-untyped]
from django.conf.urls.static import static  # type: ignore[import-untyped]
from django.urls import path  # type: ignore[import-untyped]

from appCrearteConscienteZ import views

urlpatterns: list[path] = [
    path("", views.home, name="home"),
    path("seleccion_carta/", views.seleccion_carta, name="seleccion_carta"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
