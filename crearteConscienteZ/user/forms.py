from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    nombre = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'})
    )
    apellido = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control'})
    )
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'nombre', 'apellido', 'fecha_nacimiento']
