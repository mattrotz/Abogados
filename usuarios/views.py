from django.shortcuts import render

UBICACION_USUARIO = '../Templates/usuarios/'

def user(request):
    return render(request, f'{UBICACION_USUARIO}usuario.html')