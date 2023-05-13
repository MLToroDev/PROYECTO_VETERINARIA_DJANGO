from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name="inicio"),

    path('registrar_persona/', views.RegistrarPersona),
    path('listar_persona/', views.listarPersona),

    path('signin/', views.Login)   
]