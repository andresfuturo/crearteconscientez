# Crearte ConscienteZ 🌿✨

## 📚 Descripción Técnica

**Crearte ConscienteZ** es una aplicación web desarrollada con Django que implementa un sistema de misiones y elementos espirituales. El proyecto está diseñado siguiendo las mejores prácticas de Django y Python.

## 🛠️ Requisitos Técnicos

- Python 3.12+
- Django 5.2
- SQLite (base de datos por defecto)
- Dependencias adicionales en `requirements.txt`

## 📦 Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPO]
```

2. Crear y activar entorno virtual:
```bash
python -m venv virtual
source virtual/bin/activate  # Linux/Mac
.\virtual\Scripts\activate  # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno (opcional):
```bash
cp .env.example .env
```

5. Ejecutar migraciones:
```bash
python manage.py migrate
```

6. Crear superusuario (opcional):
```bash
python manage.py createsuperuser
```

7. Iniciar servidor de desarrollo:
```bash
python manage.py runserver
```

## 📁 Estructura del Proyecto

```
crearteConscienteZ/
├── appCrearteConscienteZ/           # Aplicación principal
│   ├── migrations/                  # Migraciones de la base de datos
│   ├── static/                      # Archivos estáticos
│   ├── templates/                   # Templates HTML
│   ├── models.py                    # Modelos de datos
│   ├── views.py                     # Vistas
│   ├── urls.py                      # URLs de la aplicación
│   └── middleware.py                # Middleware personalizado
├── user/                           # Aplicación de autenticación
│   ├── migrations/                  # Migraciones de usuarios
│   ├── models.py                    # Modelos de usuarios
│   └── views.py                     # Vistas de autenticación
├── static/                         # Archivos estáticos compartidos
├── templates/                     # Templates compartidos
├── manage.py                      # Script de gestión de Django
└── crearteConscienteZ/           # Configuración del proyecto
    ├── settings.py               # Configuración de Django
    ├── urls.py                  # URLs principales
    └── wsgi.py                  # Punto de entrada WSGI
```

## 🚀 Funcionalidades Principales

1. **Sistema de Autenticación**
   - Registro de usuarios
   - Login/logout
   - Perfil de usuario

2. **Sistema de Misiones**
   - Misiones diarias
   - Sistema de progreso
   

3. **Interfaz de Usuario**
   - Diseño responsivo
   - Animaciones interactivas
   

## 💾 Base de Datos

- SQLite por defecto
- Migraciones automatizadas
- Modelo de datos optimizado
- Índices para rendimiento

## 🔧 Herramientas de Desarrollo

- Ruff para linting
- Bandit para seguridad
- Selenium para automatización
- Django Debug Toolbar



## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

#