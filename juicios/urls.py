from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='juicios_home'),  # Ruta para la vista principal de juicios
    # Otras rutas de la aplicación "juicios"
]