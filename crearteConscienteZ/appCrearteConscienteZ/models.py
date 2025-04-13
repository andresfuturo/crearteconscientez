# models.py
from django.db import models

class Avatar(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.IntegerField(default=1)
    fuego = models.BooleanField(default=False)
    agua = models.BooleanField(default=False)
    tierra = models.BooleanField(default=False)
    aire = models.BooleanField(default=False)
    # Puedes agregar otros atributos como experiencia, poderes, etc.

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'appcrearteconscientez_avatar'  # Personalizando el nombre de la tabla de avatares
