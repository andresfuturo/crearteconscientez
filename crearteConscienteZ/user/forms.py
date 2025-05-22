"""Forms para la aplicación de usuarios.

Este módulo contiene los formularios personalizados para la creación de usuarios.
"""

from typing import ClassVar

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Formulario personalizado para la creación de usuarios.

    Extiende UserCreationForm para incluir campos adicionales como nombre,
    apellido y fecha de nacimiento.
    """

    nombre = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"}),
    )
    apellido = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={"placeholder": "Apellido", "class": "form-control"}),
    )
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
    )

    class Meta:
        """Configuración meta del formulario.

        Especifica el modelo y los campos a utilizar en el formulario.
        """

        model = CustomUser
        fields: ClassVar[list[str]] = ["username", "email", "password1", "password2", "nombre", "apellido", "fecha_nacimiento"]
