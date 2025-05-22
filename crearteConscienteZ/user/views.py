"""Módulo de vistas del usuario: gestiona el registro y creación de carpetas personales."""

from pathlib import Path

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.http import HttpRequest
from django.shortcuts import render

from .forms import CustomUserCreationForm


def registro(request: HttpRequest) -> render:
    """Vista para el registro de nuevos usuarios.

    Maneja tanto el GET como el POST para mostrar el formulario de registro
    y procesar los datos del nuevo usuario. Si el registro es exitoso,
    crea una carpeta personal para el usuario.

    Args:
        request: HttpRequest que contiene los datos del formulario en caso de POST

    Returns:
        render: Renderiza la plantilla de registro con el formulario y mensajes

    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                user_folder = Path(settings.BASE_DIR) / "crearteConscienteZ" / "user" / user.username
                user_folder.mkdir(parents=True, exist_ok=True)
                return render(request, "user/registroUsuario.html", {
                    "form": CustomUserCreationForm(),
                    "registro_exitoso": True,
                    "mensaje": "Registro exitoso. Por favor, inicia sesión con tus credenciales.",
                })
            except (OSError, PermissionError) as e:
                form.add_error(None, f"Error al crear la carpeta del usuario: {e!s}")
            except (ValidationError, IntegrityError, ValueError) as e:
                form.add_error(None, f"Error al procesar el registro: {e!s}")
        else:
            # Agregar mensajes más amigables para errores específicos
            if "username" in form.errors:
                form.add_error("username", "Este nombre de usuario ya está en uso. Por favor, elige otro.")
            if "email" in form.errors:
                form.add_error("email", "Este correo electrónico ya está registrado.")
    else:
        form = CustomUserCreationForm()
    return render(request, "user/registroUsuario.html", {"form": form})
