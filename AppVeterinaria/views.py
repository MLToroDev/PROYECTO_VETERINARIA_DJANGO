from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def RegistrarPersona(request):
    return render(request, 'RegistrarPersona.html')
