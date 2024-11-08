from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import Abogados

LOCATION = '../Templates/usuarios/'


# Create your views here.
class ListarAbogados(ListView):
    model = Abogados
    template_name = f'{LOCATION}abogados.html'
    context_object_name = 'abogados'


class CrearAbogado(CreateView):
    model = Abogados
    template_name = f'{LOCATION}crear_abogados.html'
    fields = ['nombre','apellido','especialidad','foto']
    success_url = reverse_lazy('ListarAbogados')

class DetallesAbogados(DetailView):
    model = Abogados
    template_name = 'detalles_abogados.html'
    context_object_name = 'DetallesAbogados'

class ActualizarAbogado(UpdateView):
    model = Abogados
    template_name = f'{LOCATION}actualizar_abogados.html'
    fields = ['nombre','apellido','especialidad','foto']
    success_url = reverse_lazy('DetallesAbogados')




