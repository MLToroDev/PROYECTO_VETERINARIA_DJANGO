from django.urls import path
from . import views

urlpatterns = [
    path('registrar_mascota/', views.RegistrarMascota),
    path('registrar_persona/', views.RegistrarPersona),
    path('', views.Inicio, name="inicio"),
]