from django.urls import path
from .views import *

urlpatterns = [
    # URL de usuarios normales
    path('accounts/Registrarse/', RegistrosUsuarios, name='RegistroUsuarios'),
    path('accounts/Iniciar Sesion/', InicioSesionUsuarios, name='IniciarSesionUsuarios'),
    path('accounts/Cerrar Sesion/',CerrarSesion, name='CerrarSesion'),
    path('dashboard/',Dashboard, name='Dashboard'),

    # URL de servicios
    path('contratos/servicios/registrar/', RegistroServicio, name = 'RegistrarServicio'),
    path('contratos/servicios/actualizar/<int:pk>/', ActualizarServicio, name='ActualizarServicio'),
    path('contratos/servicios/borrar/<int:pk>/', BorrarServicio, name='BorrarServicio'),

    # URL de divorcios
    path('contratos/divorcios/registrar/', RegistroDivorcios, name = 'RegistrarDivorcios'),
    path('contratos/divorcios/',ListaDivorcios, name='ListaDivorcios'),
    path('contratos/divorcios/actualizar/<int:pk>/', ActualizarDivorcios, name='ActualizarDivorcios'),
    path('contratos/divorcios/borrar/<int:pk>/', BorrarDivorcios, name='BorrarDivorcios')        
]
