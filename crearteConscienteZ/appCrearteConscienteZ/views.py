from contextlib import redirect_stderr
from django.shortcuts import render # type: ignore
# Create your views here.
def home (request):
    return render(request,"home.html")

def portalDeAcceso(request):
    return render(request, 'portalDeAcceso.html')

def ayuda(request):
    return render(request, 'ayuda.html')

def registroUsuario(request):
    return render(request, "registroUsuario.html") 

def elementos(request):
    return render(request, 'elementos.html')


def elemento_agua_femenina(request):
    return render(request, 'elementosFemeninos/elemento_agua_femenina.html')

def elemento_tierra_femenina(request):
   return render(request, 'elementosFemeninos/elemento_tierra_femenina.html')

def elemento_fuego_femenina(request):
    return render(request, 'elementosFemeninos/elemento_fuego_femenina.html')

def elemento_aire_femenina(request):
    return render(request, 'elementosFemeninos/elemento_aire_femenina.html')


def mision_tierra_femenina(request):
    return render(request, 'misiones_femeninas/mision_tierra_femenina.html')

def mision_fuego_femenina(request):
    return render(request, 'misiones_femeninas/mision_fuego_femenina.html')

def mision_agua_femenina(request):
    return render(request, 'misiones_femeninas/mision_agua_femenina.html')

def mision_aire_femenina(request):
    return render(request, 'misiones_femeninas/mision_aire_femenina.html')


def elemento_fuego_masculino(request):
    return render(request, 'elementosMasculinos/elemento_fuego_masculino.html')

def elemento_tierra_masculino(request):
    return render(request, 'elementosMasculinos/elemento_tierra_masculino.html')

def elemento_aire_masculino(request):
    return render(request, 'elementosMasculinos/elemento_aire_masculino.html')

def elemento_agua_masculino(request):
    return render(request, 'elementosMasculinos/elemento_agua_masculino.html')





def mision_fuego_masculino(request):
    return render(request, 'misiones_masculinos/mision_fuego_masculino.html')

def mision_tierra_masculino(request):
    return render(request, 'misiones_masculinos/mision_tierra_masculino.html')

def mision_aire_masculino(request):
    return render(request, 'misiones_masculinos/mision_aire_masculino.html')

def mision_agua_masculino(request):
    return render(request, 'misiones_masculinos/mision_agua_masculino.html')