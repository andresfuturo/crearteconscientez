from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.utils import timezone
from user.models import ProgresoUsuario


def contacto(request):
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


def gracias (request):
    return render(request,"gracias.html")


def manual_view(request):
    return render(request, "manual.html")


# Create your views here.
def home (request):
    return render(request,"home.html")


def portalDeAcceso(request):
    print("DEBUG: Entrando a la vista portalDeAcceso")
    error = None
    if request.method == "POST":
        print("DEBUG: Método POST recibido")
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(f"DEBUG: Username recibido: {username}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("DEBUG: Usuario autenticado correctamente")
            login(request, user)
            return redirect("elementos")
        print("DEBUG: Usuario o contraseña incorrectos")
        error = "Usuario o contraseña incorrectos."
    print(f"DEBUG: Error enviado al template: {error}")
    return render(request, "portalDeAcceso.html", {"error": error})


def registroUsuario(request):
    return render(request, "registroUsuario.html")



def elementos(request):
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


def elemento_agua_femenina(request):
    return render(request, "elementosFemeninos/elemento_agua_femenina.html")

def elemento_tierra_femenina(request):
   return render(request, "elementosFemeninos/elemento_tierra_femenina.html")

def elemento_fuego_femenina(request):
    return render(request, "elementosFemeninos/elemento_fuego_femenina.html")

def elemento_aire_femenina(request):
    return render(request, "elementosFemeninos/elemento_aire_femenina.html")




def redirigir_a_mision_activa(progreso, vista_actual=None):
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
    if progreso.avatar in avatar_to_view:
        if vista_actual != avatar_to_view[progreso.avatar]:
            return redirect(avatar_to_view[progreso.avatar])
    return None

@login_required
def mision_tierra_femenina(request):
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
def mision_fuego_femenina(request):
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
def mision_agua_femenina(request):
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
def mision_aire_femenina(request):
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
def mision_tierra_masculino(request):
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
def mision_fuego_masculino(request):
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
def mision_agua_masculino(request):
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
def mision_aire_masculino(request):
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


def elemento_fuego_masculino(request):
    return render(request, "elementosMasculinos/elemento_fuego_masculino.html")

def elemento_tierra_masculino(request):
    return render(request, "elementosMasculinos/elemento_tierra_masculino.html")

def elemento_aire_masculino(request):
    return render(request, "elementosMasculinos/elemento_aire_masculino.html")

def elemento_agua_masculino(request):
    return render(request, "elementosMasculinos/elemento_agua_masculino.html")

@login_required
def seleccion_carta(request):
    return render(request, "seleccion_carta.html")




