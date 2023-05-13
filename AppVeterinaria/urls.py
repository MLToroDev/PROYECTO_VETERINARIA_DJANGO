from django.urls import path
from . import views

urlpatterns = [
    
    path('registrar_persona/', views.RegistrarPersona),
    path('listar_persona/', views.listarPersona),

]