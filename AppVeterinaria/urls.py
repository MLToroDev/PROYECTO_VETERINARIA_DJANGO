from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
      
    path('', views.menuPl, name='inicio' ),
    path('registrar_persona/', views.RegistrarPersona, name='registrar_persona'),
    path('registrar_mascota/', views.RegistarMascota, name='registrar_mascota'),
    path('registrar_factura/', views.RegistrarFactura, name='registrar_factura'),
    path('registrar_consulta/', views.RegistrarConsulta, name='registrar_consulta'),

    path('listar_persona/', views.listarPersona, name = 'listar_persona'),
    path('listar_mascota/', views.listarMascota, name = 'listar_mascota'),
    path('listar_factura/', views.listarFactura, name = 'listar_factura'),
    path('listar_consulta/', views.listarConsulta, name = 'listar_consulta'),
    
]