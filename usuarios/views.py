# Importacion de modelos
from django.contrib.auth.models import User
from .models import Abogados

# Importacion de renderizado de vistas
from django.shortcuts import render, redirect

# Importacion de autenticacion del usuario
from django.contrib.auth import login, logout, authenticate

# Importacion de manejo de errores
from django.db import IntegrityError

UBICACION_LOGUEO = "../Templates/"
UBICACION_ADMIN = "../Templates/usuarios/admin/"
UBICACION_USUARIOS = "../Templates/usuarios/clientes/"
UBICACION_ABOGADOS = "../Templates/abogados/"


# Create your views here


# Logica para las vistas para el registrar y iniciar
class VistasUsuario:

    def __init__(self, request):
        self.request = request

    def Registro(self):
        if self.request.POST["pass1"] == self.request.POST["pass2"]:
            nombre = self.request.POST["nombre"]
            contra = self.request.POST["pass1"]
            ModelUser = User.objects.create_user(username=nombre, password=contra)
            try:
                ModelUser.save()
                login(self.request, ModelUser)
                return redirect("DashboardUser")
            except IntegrityError:
                return render(
                    self.request,
                    f"{UBICACION_LOGUEO}registrarse.html",
                    {"Error": "Usuario creado"},
                )
        else:
            return render(
                self.request,
                f"{UBICACION_LOGUEO}registrarse.html",
                {"Error": "Las contraseñas no coinciden"},
            )

    def InicioSesion(self):
        nombre = self.request.POST["nombre"]
        contra = self.request.POST["pass"]
        auth = authenticate(username=nombre, password=contra)
        if auth is not None:
            login(self.request, auth)
            if auth.is_superuser:
                return redirect("DashboardAdmin")
            else:
                return redirect("DashboardUser")
        else:
            return render(
                self.request,
                f"{UBICACION_LOGUEO}iniciar_sesion.html",
                {"Error": "Usuario o contraseña no coinciden"},
            )

    def CierreSesion(self):
        logout(self.request)
        return redirect("Inicio")

# Logica para las vistas del superadmin con el
class VistasDeAbogados:
    def __init__(self, request):
        self.request = request


    def ListarAbogados(self):
        listaAbogados = Abogados.objects.all()
        return listaAbogados

    def CrearAbogados(self):
        nombre = self.request.POST['nombre']
        apellido = self.request.POST['apellido']
        especialidad = self.request.POST['especialidad']
        ModeloAbogado = Abogados.objects.create(
            nombre = nombre,
            apellido = apellido,
            especialidad = especialidad
        )
        if ModeloAbogado:
            return redirect('DashboardAdmin')
        else:
            return render(self.request, f'{UBICACION_ABOGADOS}crear_abogados.html',{
                'Error': 'Error al guardar abogado'
            })

        

    def DetallesAbogados(self, id):
        datosAbogado = Abogados.objects.get(id=id)
        return datosAbogado

    def ActualizarAbogados(self, id):
        abogadoActualizar = Abogados.objects.get(id = id)
        abogadoActualizar.nombre = self.request.POST['nombre']
        abogadoActualizar.apellido = self.request.POST['apellido']
        abogadoActualizar.especialidad = self.request.POST['especialidad']
        abogadoActualizar.save()
        return redirect('DashboardAdmin')
    
    def BorrarAbogados(self,id):
        abogadoBorrar = Abogados.objects.get(id=id).delete()
        if abogadoBorrar is None:
            return False
        else:
            return True



# Vistas


def RegistrosUsuarios(request):
    if request.method == "GET":
        return render(request, f"{UBICACION_LOGUEO}registrarse.html")
    else:
        Usuarios = VistasUsuario(request)
        return Usuarios.Registro()


def InicioSesionUsuarios(request):
    if request.method == "GET":
        return render(request, f"{UBICACION_LOGUEO}iniciar_sesion.html")
    else:
        Usuarios = VistasUsuario(request)
        return Usuarios.InicioSesion()


def CerrarSesion(request):
    Usuarios = VistasUsuario(request)
    return Usuarios.CierreSesion()


def DashboardUser(request):
    if request.method == "GET":
        return render(request, f"{UBICACION_USUARIOS}dashboard.html")


def DashboardAdmin(request):
    if request.method == "GET":
        VistasAbogados= VistasDeAbogados(request)
        listaAbogados = VistasAbogados.ListarAbogados() 
        return render(request, f"{UBICACION_ADMIN}dashboard.html",{
            'listaAbogados': listaAbogados
        })

    
def CrearAbogados(request):
    vistaAbogado = VistasDeAbogados(request)
    if request.method == "GET":
        return render(request,f'{UBICACION_ABOGADOS}crear_abogados.html')
    else:
        return vistaAbogado.CrearAbogados()

def DetallesAbogados(request,pk):
    vistaAbogado = VistasDeAbogados(request)
    response =  vistaAbogado.DetallesAbogados(pk)
    return render(request,f'{UBICACION_ABOGADOS}detalles_abogados.html',{
        'DetallesAbogados' : response
    })
    
def ActualizarAbogados(request,pk):
    vistaAbogado = VistasDeAbogados(request)
    response = vistaAbogado.DetallesAbogados(pk)
    if request.method == "GET":
        return render(request,f'{UBICACION_ABOGADOS}actualizar_abogados.html',{
            'detalles': response
        })
    else:
        return vistaAbogado.ActualizarAbogados(pk)
    
def BorrarAbogados(request,pk):
    vistaAbogado = VistasDeAbogados(request)
    response = vistaAbogado.BorrarAbogados(pk)
    if response == True:
        return redirect('DashboardAdmin')
    else:
        return render(request, f'{UBICACION_ADMIN}dashboard.html',{
            'Error':'Error al borrar el registro'
        })
    




