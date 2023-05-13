from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def RegistrarPersona(request):
    return render(request, 'Persona/RegistrarPersona.html')

def listarPersona(request):
    return render(request, 'Persona/TablaPersona.html')

def signin(request):
    return render(request, 'Login.html')

