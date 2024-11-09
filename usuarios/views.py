from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import Abogados

UBICACION_USUARIOS = '../Templates/usuarios/clientes/'
UBICACION_ABOGADOS = '../Templates/abogados/'


# Create your views here

#Vistas para el signup
class RegistrosUsuarios(CreateView):
    form_class = UserCreationForm
    template_name = f'{UBICACION_USUARIOS}registrarse.html'
    success_url = reverse_lazy('IniciarSesionUsuarios')


class ListarAbogados(ListView):
    model = Abogados
    template_name = f'{UBICACION_ABOGADOS}abogados.html'
    context_object_name = 'abogados'


class CrearAbogado(CreateView):
    model = Abogados
    template_name = f'{UBICACION_ABOGADOS}crear_abogados.html'
    fields = ['nombre','apellido','especialidad','foto']
    success_url = reverse_lazy('ListarAbogados')

class DetallesAbogados(DetailView):
    model = Abogados
    template_name = 'detalles_abogados.html'
    context_object_name = 'DetallesAbogados'

class ActualizarAbogado(UpdateView):
    model = Abogados
    template_name = f'{UBICACION_ABOGADOS}actualizar_abogados.html'
    fields = ['nombre','apellido','especialidad','foto']
    success_url = reverse_lazy('DetallesAbogados')




