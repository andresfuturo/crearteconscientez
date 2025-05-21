import os

from django.conf import settings
from django.shortcuts import render

from .forms import CustomUserCreationForm


def registro(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                user_folder = os.path.join(settings.BASE_DIR, "crearteConscienteZ", "user", user.username)
                os.makedirs(user_folder, exist_ok=True)
                return render(request, "user/registroUsuario.html", {
                    "form": CustomUserCreationForm(),
                    "registro_exitoso": True,
                    "mensaje": "Registro exitoso. Por favor, inicia sesión con tus credenciales.",
                })
            except Exception as e:
                form.add_error(None, f"Error al crear la cuenta: {e!s}")
        else:
            # Agregar mensajes más amigables para errores específicos
            if "username" in form.errors:
                form.add_error("username", "Este nombre de usuario ya está en uso. Por favor, elige otro.")
            if "email" in form.errors:
                form.add_error("email", "Este correo electrónico ya está registrado.")
    else:
        form = CustomUserCreationForm()
    return render(request, "user/registroUsuario.html", {"form": form})
