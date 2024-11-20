# Importacion de modelos
from django.contrib.auth.models import User
from .models import ServicioLegal, Divorcio

# Importacion de renderizado de vistas
from django.shortcuts import render, redirect

# Importacion de autenticacion del usuario
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Importacion de manejo de errores
from django.db import IntegrityError

UBICACION_LOGUEO = "../Templates/autenticacion/"
UBICACION_USUARIOS = "../Templates/usuarios/"
UBICACION_SERVICIOS = "../Templates/servicios/"
UBICACION_DIVORCIOS = "../Templates/servicios/divorcios"


# Create your views here


# Logica para las vistas para el registrar y iniciar
class VistasUsuario:

    def __init__(self,request):
        self.request = request

    def Registro(self):
        if self.request.POST["pass1"] == self.request.POST["pass2"]:
            nombre = self.request.POST["nombre"]
            contra = self.request.POST["pass1"]
            ModelUser = User.objects.create_user(username=nombre, password=contra)
            try:
                ModelUser.save()
                login(self.request, ModelUser)
                return redirect("Dashboard")
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
            return redirect("Dashboard")
        else:
            return render(
                self.request,
                f"{UBICACION_LOGUEO}iniciar_sesion.html",
                {"Error": "Usuario o contraseña no coinciden"},
            )

    def CierreSesion(self):
        logout(self.request)
        return redirect("Inicio")

# Logica para las vistas de los servicios
class VistaDeServiciosLegales:

    @staticmethod
    def RegistroServicio(request,model):

        # Obtencion de datos desde el formulario
        servicioFormulario = request.POST["Servicio"]
        DescripcionFormulario = request.POST["Descripcion"]
        CostoServicio = request.POST["Costo"]

        # Guardado de datos
        try:
            model.objects.create(
                nombreServicio=servicioFormulario,
                descripcionServicio=DescripcionFormulario,
                costoServicio=CostoServicio,
            )
            return f"Servicio registrado exitosamente"
        except IntegrityError:
            return "Error: no se pudo guardar el caso"

    @staticmethod
    def ListaDeServicios(model):
            return model.objects.all()

    @staticmethod
    def DetallesDeServicios(model,pk):
        return model.objects.get(id=pk)

    @staticmethod
    def ActualizarServicios(request,model,pk):
        ServicioActualizar = model.objects.get(id=pk)
        try:
            ServicioActualizar.nombreServicio = request.POST["Servicio"]
            ServicioActualizar.descripcionServicio = request.POST["Descripcion"]
            ServicioActualizar.costoServicio = request.POST["Costo"]
            ServicioActualizar.save()
        except IntegrityError:
            return f"Error al actualizar"

    @staticmethod
    def BorrarServicio(model, pk):
        try:
            servicio = model.objects.get(id=pk)
            servicio.delete()
        except IntegrityError:
            return "Error al borrar"

# Logica para las vistas de divocios

class VistaDeDivorcios(VistaDeServiciosLegales):

    @staticmethod
    def RegistroServicios(request, model):
        servicio = request.POST['Servicio']
        descripcion = request.POST['Descripcion']
        costo = request.POST['Costo']
        duracion = request.POST['Duracion']

        try:
            model.objects.create(
                nombreServicio = servicio,
                descripcionServicio = descripcion,
                costoServicio = costo,
                duracion = duracion
            )
        except:
            return 'Error'
        
    @staticmethod
    def ListaDivorcios(model):
        return VistaDeServiciosLegales.ListaDeServicios(model)
    
    @staticmethod
    def DetallesDivorcios(model,pk):
        return VistaDeServiciosLegales.DetallesDeServicios(model,pk)
    
    @staticmethod
    def ActualizarDivorcio(request,model,pk):
        DivorcioActualizar = model.objects.get(id=pk)
        try:
            DivorcioActualizar.nombreServicio = request.POST["Servicio"]
            DivorcioActualizar.descripcionServicio = request.POST["Descripcion"]
            DivorcioActualizar.costoServicio = request.POST["Costo"]
            DivorcioActualizar.duracion = request.POST['Duracion']
            DivorcioActualizar.save()
        except IntegrityError:
            return f"Error al actualizar"

    @staticmethod
    def BorrarDivorcio(model,pk):
        try:
            divorcio = model.objects.get(id=pk)
            divorcio.delete()
        except IntegrityError:
            return "Error al borrar"
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

@login_required
def Dashboard(request):
    Servicios = VistaDeServiciosLegales.ListaDeServicios(ServicioLegal)
    Divorcios = VistaDeDivorcios.ListaDivorcios(Divorcio)
    return render(request, f"{UBICACION_USUARIOS}dashboard.html", {"Servicios": Servicios, 'Divorcios':Divorcios})

# VISTAS DE SERVICIOS

@login_required
def RegistroServicio(request):
    if request.method == "GET":
        return render(request, f"{UBICACION_SERVICIOS}registrar_servicios.html")
    else:
        VistaDeServiciosLegales.RegistroServicio(request,ServicioLegal)
        return redirect("Dashboard")

@login_required
def ListaDeServicios(request):
    Servicios = VistaDeServiciosLegales.ListaDeServicios(ServicioLegal)
    return render(
        request,
        f"{UBICACION_SERVICIOS}servicios_usuarios.html",
        {"Servicios": Servicios},
    )

@login_required
def ActualizarServicio(request, pk):
    if request.method == "GET":
        print(request)
        datosFormulario = VistaDeServiciosLegales.DetallesDeServicios(ServicioLegal,pk)
        return render(
            request,
            f"{UBICACION_SERVICIOS}actualizar_servicios.html",
            {"DatosFormulario": datosFormulario},
        )
    else:
        VistaDeServiciosLegales.ActualizarServicios(request,ServicioLegal,pk)
        return redirect("Dashboard")

@login_required
def BorrarServicio(request, pk):
    if request.method == "GET":
        return render(request, f"{UBICACION_SERVICIOS}confirmacion_borrar.html")
    else:
        VistaDeServiciosLegales.BorrarServicio(ServicioLegal,pk)
        return redirect("Dashboard")


@login_required
def RegistroDivorcios(request):
    if request.method == 'GET':
        return render(request,f'{UBICACION_DIVORCIOS}/registrar_divorcio.html')
    else:
        VistaDeDivorcios.RegistroServicios(request,Divorcio)
        return redirect('Dashboard')

@login_required
def ListaDivorcios(request):
    Servicios = VistaDeDivorcios.ListaDivorcios(Divorcio)
    return render(
        request,
        f"{UBICACION_DIVORCIOS}servicios_usuarios.html",
        {"Servicios": Servicios},
    )

@login_required
def ActualizarDivorcios(request, pk):
    if request.method == "GET":
        print(request)
        datosFormulario = VistaDeDivorcios.DetallesDivorcios(Divorcio,pk)
        return render(
            request,
            f"{UBICACION_DIVORCIOS}/actualizar_divorcio.html",
            {"DatosFormulario": datosFormulario},
        )
    else:
        VistaDeDivorcios.ActualizarDivorcio(request,Divorcio,pk)
        return redirect("Dashboard")

@login_required
def BorrarDivorcios(request, pk):
    if request.method == "GET":
        return render(request, f"{UBICACION_DIVORCIOS}/confirmacion_borrar.html")
    else:
        VistaDeDivorcios.BorrarDivorcio(Divorcio,pk)
        return redirect("Dashboard")

