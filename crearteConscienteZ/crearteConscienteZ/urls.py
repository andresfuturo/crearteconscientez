"""
URL configuration for crearteConscieteZ project.

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
from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore

from appCrearteConscienteZ import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appCrearteConscienteZ.urls')),
    path('', views.home, name='home'),
    path('portalDeAcceso/', views.portalDeAcceso, name='portalDeAcceso'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('elementos/', views.elementos, name='elementos'),
    path('portalDeAcceso/registroUsuario/', views.registroUsuario, name='registroUsuario'),
    
    path('elemento_agua_femenina/', views.elemento_agua_femenina, name='elemento_agua_femenina'),
    path('elemento_tierra_femenina/', views.elemento_tierra_femenina, name='elemento_tierra_femenina'),
    path('elemento_fuego_femenina/', views.elemento_fuego_femenina, name='elemento_fuego_femenina'),
    path('elemento_aire_femenina/', views.elemento_aire_femenina, name='elemento_aire_femenina'),

    path('mision_tierra_femenina/', views.mision_tierra_femenina, name='mision_tierra_femenina'),
    path('mision_fuego_femenina/', views.mision_fuego_femenina, name='mision_fuego_femenina'),
    path('mision_agua_femenina/', views.mision_agua_femenina, name='mision_agua_femenina'),
    path('mision_aire_femenina/', views.mision_aire_femenina, name='mision_aire_femenina'),

    path('elemento_fuego_masculino/', views.elemento_fuego_masculino, name='elemento_fuego_masculino'),
    path('elemento_tierra_masculino/', views.elemento_tierra_masculino, name='elemento_tierra_masculino'),
    path('elemento_aire_masculino/', views.elemento_aire_masculino, name='elemento_aire_masculino'),
     path('elemento_agua_masculino/', views.elemento_agua_masculino, name='elemento_agua_masculino'),


    path('mision_fuego_masculino/', views.mision_fuego_masculino, name='mision_fuego_masculino'),
    path('mision_tierra_masculino/', views.mision_tierra_masculino, name='mision_tierra_masculino'),
    path('mision_aire_masculino/', views.mision_aire_masculino, name='mision_aire_masculino'),
    path('mision_agua_masculino/', views.mision_agua_masculino, name='mision_agua_masculino'),
]
