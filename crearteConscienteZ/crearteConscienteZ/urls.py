"""URL configuration for crearteConscienteZ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from appCrearteConscienteZ import views as app_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import include, path
from user import views as user_views


def custom_404(request: HttpRequest, _exception: Exception) -> HttpResponse:
    """Maneja errores 404 renderizando una página personalizada.

    Args:
        request: La solicitud HTTP entrante
        _exception: La excepción que causó el error 404 (no utilizado)

    Returns:
        HttpResponse: Una respuesta 404 con la plantilla personalizada
    """
    return render(request, "404.html", status=404)

handler404 = custom_404

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", app_views.home, name="home"),
    path("", include("appCrearteConscienteZ.urls")),
    path("portalDeAcceso/", app_views.portalDeAcceso, name="portalDeAcceso"),
    path("contacto/", app_views.contacto, name="contacto"),
    path("gracias/", app_views.gracias, name="gracias"),
    path("elementos/", app_views.elementos, name="elementos"),
    path("portalDeAcceso/registroUsuario/", user_views.registro, name="registroUsuario"),

    path("elemento_agua_femenina/", app_views.elemento_agua_femenina, name="elemento_agua_femenina"),
    path("elemento_tierra_femenina/", app_views.elemento_tierra_femenina, name="elemento_tierra_femenina"),
    path("elemento_fuego_femenina/", app_views.elemento_fuego_femenina, name="elemento_fuego_femenina"),
    path("elemento_aire_femenina/", app_views.elemento_aire_femenina, name="elemento_aire_femenina"),

    path("mision_tierra_femenina/", app_views.mision_tierra_femenina, name="mision_tierra_femenina"),
    path("mision_fuego_femenina/", app_views.mision_fuego_femenina, name="mision_fuego_femenina"),
    path("mision_agua_femenina/", app_views.mision_agua_femenina, name="mision_agua_femenina"),
    path("mision_aire_femenina/", app_views.mision_aire_femenina, name="mision_aire_femenina"),

    path("elemento_fuego_masculino/", app_views.elemento_fuego_masculino, name="elemento_fuego_masculino"),
    path("elemento_tierra_masculino/", app_views.elemento_tierra_masculino, name="elemento_tierra_masculino"),
    path("elemento_aire_masculino/", app_views.elemento_aire_masculino, name="elemento_aire_masculino"),
     path("elemento_agua_masculino/", app_views.elemento_agua_masculino, name="elemento_agua_masculino"),


    path("mision_fuego_masculino/", app_views.mision_fuego_masculino, name="mision_fuego_masculino"),
    path("mision_tierra_masculino/", app_views.mision_tierra_masculino, name="mision_tierra_masculino"),
    path("mision_aire_masculino/", app_views.mision_aire_masculino, name="mision_aire_masculino"),
    path("mision_agua_masculino/", app_views.mision_agua_masculino, name="mision_agua_masculino"),

    path("usuarios/", include("user.urls")),
    path("manual/", app_views.manual_view, name="manual"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
