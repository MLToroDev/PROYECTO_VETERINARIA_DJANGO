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

def exit(request):
    logout(request)
    return redirect('bienvenida')











