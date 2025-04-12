# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    tipo_sangre = models.CharField(max_length=10, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
