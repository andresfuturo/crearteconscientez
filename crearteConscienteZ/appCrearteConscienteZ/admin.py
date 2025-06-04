
"""Administración de la aplicación Crearte ConscienteZ.

Este módulo configura la interfaz de administración de Django para los modelos de la aplicación.
"""

# Register your models here.
from django.contrib import admin

# Cambiar el encabezado y título del sitio admin
admin.site.site_header = "Crearte ConscienteZ"
admin.site.site_title = "Administrador de Crearte ConscienteZ"
admin.site.index_title = "Bienvenido al Panel de Crearte ConscienteZ"
