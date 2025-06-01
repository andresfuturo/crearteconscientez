"""Módulo de vistas de la aplicación Crearte ConscienteZ.

Este módulo contiene todas las vistas de la aplicación, incluyendo:
- Sistema de autenticación (login/registro)
- Sistema de misiones (elementos Femeninos y Masculinos)
- Páginas estáticas (contacto, manual, home)
- Sistema de avatares y progreso del usuario
"""

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.utils import timezone
from user.models import ProgresoUsuario

def custom_404(request, exception):
    return render(request, '404.html', status=404)



def contacto(request: HttpRequest) -> render:
    """Formulario de contacto.

    Maneja el envío de mensajes de contacto y redirige a la página de agradecimiento.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista del formulario de contacto o redirección a la página de agradecimiento.
    """
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        # Agregamos nombre y email al mensaje:
        message = f"Mensaje de: {name}\nEmail: {email}\n\n{message}"

        from_email = settings.EMAIL_HOST_USER
        recipient_list = ["crearteconscientez@gmail.com"]

        send_mail(subject, message, from_email, recipient_list)

        return render(request, "gracias.html")

    return render(request, "contacto.html")


def gracias(request: HttpRequest) -> render:
    """Página de agradecimiento.

    Muestra una página de agradecimiento después de enviar el formulario de contacto.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista de la página de agradecimiento.
    """
    return render(request,"gracias.html")


def manual_view(request: HttpRequest) -> render:
    """Página del manual.

    Muestra el manual de uso de la aplicación.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista del manual.
    """
    return render(request, "manual.html")


# Create your views here.
def home(request: HttpRequest) -> render:
    """Página principal del sitio.

    Muestra la página de inicio del sitio web.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista de la página de inicio.
    """
    return render(request,"home.html")


def portalDeAcceso(request: HttpRequest) -> render:
    """Página de portal de acceso.

    Maneja el inicio de sesión de usuarios y redirige a la página de elementos.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista del portal de acceso o redirección a elementos.
    """
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("elementos")
        error = "Usuario o contraseña incorrectos."
    return render(request, "portalDeAcceso.html", {"error": error})


def registroUsuario(request: HttpRequest) -> render:
    """Página de registro de usuario.

    Muestra el formulario de registro de usuario.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista del formulario de registro.
    """
    return render(request, "registroUsuario.html")



def elementos(request: HttpRequest) -> render:
    """Página principal de elementos.

    Muestra la página de elementos y redirige a la misión activa si existe.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista de la página de elementos.
    """
    if request.user.is_authenticated:
        try:
            progreso = ProgresoUsuario.objects.get(user=request.user)
            if progreso.mision_iniciada:
                redir = redirigir_a_mision_activa(progreso)
                if redir:
                    return redir
        except ProgresoUsuario.DoesNotExist:
            pass
    return render(request, "elementos.html")


def elemento_agua_femenina(request: HttpRequest) -> render:
    """Página del elemento Agua Femenino.

    Muestra la información sobre el elemento Agua Femenino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista del elemento Agua Femenino.
    """
    return render(request, "elementosFemeninos/elemento_agua_femenina.html")


def elemento_tierra_femenina(request: HttpRequest) -> render:
    """Página del elemento Tierra Femenino.

    Muestra la información sobre el elemento Tierra Femenino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista del elemento Tierra Femenino.
    """
    return render(request, "elementosFemeninos/elemento_tierra_femenina.html")


def elemento_fuego_femenina(request: HttpRequest) -> render:
    """Página del elemento Fuego Femenino.

    Muestra la información sobre el elemento Fuego Femenino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista del elemento Fuego Femenino.
    """
    return render(request, "elementosFemeninos/elemento_fuego_femenina.html")


def elemento_aire_femenina(request: HttpRequest) -> render:
    """Página del elemento Aire Femenino.

    Muestra la información sobre el elemento Aire Femenino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista del elemento Aire Femenino.
    """
    return render(request, "elementosFemeninos/elemento_aire_femenina.html")


def redirigir_a_mision_activa(progreso: ProgresoUsuario, vista_actual: str | None = None) -> str:
    """Redirige al usuario a la misión activa.

    Determina y redirige al usuario a la misión activa basada en su progreso.

    Args:
        progreso: El objeto ProgresoUsuario del usuario actual.
        vista_actual: La vista actual desde la que se llama a la función.

    Returns:
        str: El nombre de la vista a la que redirigir.
    """
    avatar_to_view = {
        "aire_femenina": "mision_aire_femenina",
        "fuego_femenina": "mision_fuego_femenina",
        "agua_femenina": "mision_agua_femenina",
        "tierra_femenina": "mision_tierra_femenina",
        "aire_masculino": "mision_aire_masculino",
        "fuego_masculino": "mision_fuego_masculino",
        "agua_masculino": "mision_agua_masculino",
        "tierra_masculino": "mision_tierra_masculino",
    }
    if progreso.avatar in avatar_to_view and vista_actual != avatar_to_view[progreso.avatar]:
        return redirect(avatar_to_view[progreso.avatar])
    return None

@login_required
def mision_tierra_femenina(request: HttpRequest) -> render:
    """Misión Tierra Femenino.

    Gestiona la misión del elemento Tierra Femenino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista de la misión Tierra Femenino.
    """
    user = request.user
    progreso, created = ProgresoUsuario.objects.get_or_create(user=user)
    if progreso.mision_iniciada:
        redir = redirigir_a_mision_activa(progreso, "mision_tierra_femenina")
        if redir:
            return redir
    if not progreso.mision_iniciada:
        progreso.avatar = "tierra_femenina"
        progreso.mision_iniciada = True
        progreso.mision_inicio_fecha = timezone.now()
        progreso.save()
    return render(request, "misiones_femeninas/mision_tierra_femenina.html")

@login_required
def mision_fuego_femenina(request: HttpRequest) -> render:
    """Misión Fuego Femenino.

    Gestiona la misión del elemento Fuego Femenino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista de la misión Fuego Femenino.
    """
    user = request.user
    progreso, created = ProgresoUsuario.objects.get_or_create(user=user)
    if progreso.mision_iniciada:
        redir = redirigir_a_mision_activa(progreso, "mision_fuego_femenina")
        if redir:
            return redir
    if not progreso.mision_iniciada:
        progreso.avatar = "fuego_femenina"
        progreso.mision_iniciada = True
        progreso.mision_inicio_fecha = timezone.now()
        progreso.save()
    return render(request, "misiones_femeninas/mision_fuego_femenina.html")

@login_required
def mision_agua_femenina(request: HttpRequest) -> render:
    """Misión Agua Femenino.

    Gestiona la misión del elemento Agua Femenino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista de la misión Agua Femenino.
    """
    user = request.user
    progreso, created = ProgresoUsuario.objects.get_or_create(user=user)
    if progreso.mision_iniciada:
        redir = redirigir_a_mision_activa(progreso, "mision_agua_femenina")
        if redir:
            return redir
    if not progreso.mision_iniciada:
        progreso.avatar = "agua_femenina"
        progreso.mision_iniciada = True
        progreso.mision_inicio_fecha = timezone.now()
        progreso.save()
    return render(request, "misiones_femeninas/mision_agua_femenina.html")

@login_required
def mision_aire_femenina(request: HttpRequest) -> render:
    """Misión Aire Femenino.

    Gestiona la misión del elemento Aire Femenino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista de la misión Aire Femenino.
    """
    user = request.user
    progreso, created = ProgresoUsuario.objects.get_or_create(user=user)
    if progreso.mision_iniciada:
        redir = redirigir_a_mision_activa(progreso, "mision_aire_femenina")
        if redir:
            return redir
    if not progreso.mision_iniciada:
        progreso.avatar = "aire_femenina"
        progreso.mision_iniciada = True
        progreso.mision_inicio_fecha = timezone.now()
        progreso.save()
    return render(request, "misiones_femeninas/mision_aire_femenina.html")

@login_required
def mision_tierra_masculino(request: HttpRequest) -> render:
    """Misión Tierra Masculino.

    Gestiona la misión del elemento Tierra Masculino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista de la misión Tierra Masculino.
    """
    user = request.user
    progreso, created = ProgresoUsuario.objects.get_or_create(user=user)
    if progreso.mision_iniciada:
        redir = redirigir_a_mision_activa(progreso, "mision_tierra_masculino")
        if redir:
            return redir
    if not progreso.mision_iniciada:
        progreso.avatar = "tierra_masculino"
        progreso.mision_iniciada = True
        progreso.mision_inicio_fecha = timezone.now()
        progreso.save()
    return render(request, "misiones_masculinos/mision_tierra_masculino.html")

@login_required
def mision_fuego_masculino(request: HttpRequest) -> render:
    """Misión Fuego Masculino.

    Gestiona la misión del elemento Fuego Masculino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista de la misión Fuego Masculino.
    """
    user = request.user
    progreso, created = ProgresoUsuario.objects.get_or_create(user=user)
    if progreso.mision_iniciada:
        redir = redirigir_a_mision_activa(progreso, "mision_fuego_masculino")
        if redir:
            return redir
    if not progreso.mision_iniciada:
        progreso.avatar = "fuego_masculino"
        progreso.mision_iniciada = True
        progreso.mision_inicio_fecha = timezone.now()
        progreso.save()
    return render(request, "misiones_masculinos/mision_fuego_masculino.html")

@login_required
def mision_agua_masculino(request: HttpRequest) -> render:
    """Misión Agua Masculino.

    Gestiona la misión del elemento Agua Masculino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista de la misión Agua Masculino.
    """
    user = request.user
    progreso, created = ProgresoUsuario.objects.get_or_create(user=user)
    if progreso.mision_iniciada:
        redir = redirigir_a_mision_activa(progreso, "mision_agua_masculino")
        if redir:
            return redir
    if not progreso.mision_iniciada:
        progreso.avatar = "agua_masculino"
        progreso.mision_iniciada = True
        progreso.mision_inicio_fecha = timezone.now()
        progreso.save()
    return render(request, "misiones_masculinos/mision_agua_masculino.html")

@login_required
def mision_aire_masculino(request: HttpRequest) -> render:
    """Misión Aire Masculino.

    Gestiona la misión del elemento Aire Masculino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista de la misión Aire Masculino.
    """
    user = request.user
    progreso, created = ProgresoUsuario.objects.get_or_create(user=user)
    if progreso.mision_iniciada:
        redir = redirigir_a_mision_activa(progreso, "mision_aire_masculino")
        if redir:
            return redir
    if not progreso.mision_iniciada:
        progreso.avatar = "aire_masculino"
        progreso.mision_iniciada = True
        progreso.mision_inicio_fecha = timezone.now()
        progreso.save()
    return render(request, "misiones_masculinos/mision_aire_masculino.html")


def elemento_fuego_masculino(request: HttpRequest) -> render:
    """Página del elemento Fuego Masculino.

    Muestra la información sobre el elemento Fuego Masculino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista del elemento Fuego Masculino.
    """
    return render(request, "elementosMasculinos/elemento_fuego_masculino.html")

def elemento_tierra_masculino(request: HttpRequest) -> render:
    """Página del elemento Tierra Masculino.

    Muestra la información sobre el elemento Tierra Masculino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista del elemento Tierra Masculino.
    """
    return render(request, "elementosMasculinos/elemento_tierra_masculino.html")

def elemento_aire_masculino(request: HttpRequest) -> render:
    """Página del elemento Aire Masculino.

    Muestra la información sobre el elemento Aire Masculino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista del elemento Aire Masculino.
    """
    return render(request, "elementosMasculinos/elemento_aire_masculino.html")

def elemento_agua_masculino(request: HttpRequest) -> render:
    """Página del elemento Agua Masculino.

    Muestra la información sobre el elemento Agua Masculino.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista del elemento Agua Masculino.
    """
    return render(request, "elementosMasculinos/elemento_agua_masculino.html")

@login_required
def seleccion_carta(request: HttpRequest) -> render:
    """Selección de carta.

    Permite al usuario seleccionar una carta.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        render: La vista de selección de carta.
    """
    return render(request, "seleccion_carta.html")




