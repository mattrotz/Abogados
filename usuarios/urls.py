from django.contrib import admin
from django.urls import path
from .views import (CrearAbogado,ListarAbogados, DetallesAbogados,ActualizarAbogado)

urlpatterns = [
    path('abogados/', ListarAbogados.as_view(), name='ListarAbogados'),
    path('crearAbogados/',CrearAbogado.as_view(),name='CrearAbogados'),
    path('detallesAbogados/', DetallesAbogados.as_view(), name='DetallesAbogados'),
    path('actualizarAbogado/<int:pk>/', ActualizarAbogado.as_view(), name='ActualizarAbogados')
    
]
