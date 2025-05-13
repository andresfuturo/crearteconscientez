# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ('username', 'password')}),
        ('Personal Information', {
            "fields": (
                'first_name', 'last_name', 'email',
                'nombre', 'apellido', 'fecha_nacimiento'
            )
        }),
        ('Permissions', {"fields": ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {"fields": ('last_login', 'date_joined')}),
    )
