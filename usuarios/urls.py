from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # URL de usuarios normales
    path('accounts/Registrarse/', views.RegistrosUsuarios, name='RegistroUsuarios'),
    path('accounts/Iniciar Sesion/', views.InicioSesionUsuarios, name='IniciarSesionUsuarios'),
    path('accounts/Cerrar Sesion/',views.CerrarSesion, name='CerrarSesion'),
    path('dashboard/User/',views.DashboardUser, name='DashboardUser'),
    path('dashboard/Admin/',views.DashboardAdmin, name='DashboardAdmin'),

    # URL de superAdmin
    path('crearAbogados/',views.CrearAbogados,name='CrearAbogados'),
    path('detallesAbogados/<int:pk>', views.DetallesAbogados, name='DetallesAbogados'),
    path('actualizarAbogado/<int:pk>',views.ActualizarAbogados, name='ActualizarAbogados'),
    path('borrarAbogado/<int:pk>',views.BorrarAbogados, name='BorrarAbogados'),    
]
