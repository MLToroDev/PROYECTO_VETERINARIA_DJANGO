from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group 
from django.contrib.auth import logout
from .models import Persona

# Create your views here.

def bienvenida(request):
    return render(request, 'bienvenida.html')

@login_required
def menuPl(request):
    return render(request, 'index.html')

def RegistrarPersona(request):
    return render(request, 'Persona/RegistrarPersona.html')


def listarPersona(request):
    return render(request, 'Persona/TablaPersona.html')

#-------------------------------------------------------------

def RegistarMascota(request):
    return render(request, 'Mascota/RegistrarMascota.html')

def listarMascota(request):
    return render(request, 'Mascota/TablaMascota.html')

#-------------------------------------------------------------

def RegistrarFactura(request):
    return render(request, 'Factura/RegistrarFactura.html')

def listarFactura(request):
    return render(request, 'Factura/TablaFactura.html')    

#-------------------------------------------------------------

def RegistrarConsulta(request):
    return render(request, 'Registro/RegistroConsulta.html')

def listarConsulta(request):
    return render(request, 'Registro/TablaRegistroConsulta.html')     











