from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def Inicio(request):
    return render(request, 'index.html')

def RegistrarPersona(request):
    return render(request, 'RegistrarPersona.html')

def RegistrarMascota(request):
    return render(request, 'RegistrarMascota.html')
