from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='usuarios_profile'),  # Ruta para la vista principal de usuarios
    # Otras rutas de la aplicación "usuarios"
]
