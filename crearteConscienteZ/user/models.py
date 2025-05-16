# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(null=True, blank=True)


#progreso del usuario escoge un elemento
class ProgresoUsuario(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=30, choices=[
        ('aire_femenina', 'Aire Femenina'),
        ('fuego_femenina', 'Fuego Femenina'),
        ('agua_femenina', 'Agua Femenina'),
        ('tierra_femenina', 'Tierra Femenina'),
    
    ])
    mision_iniciada = models.BooleanField(default=False)
    mision_inicio_fecha = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.avatar} - {'Iniciada' if self.mision_iniciada else 'No iniciada'}"

