from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

import os
from django.conf import settings

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print("POST data:", request.POST)
        if form.is_valid():
            print("Formulario válido")
            user = form.save()
            user_folder = os.path.join(settings.BASE_DIR, 'crearteConscienteZ', 'user', user.username)
            os.makedirs(user_folder, exist_ok=True)
            return render(request, 'user/registroUsuario.html', {'form': CustomUserCreationForm(), 'registro_exitoso': True})
        else:
            print("Errores del formulario:", form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/registroUsuario.html', {'form': form})