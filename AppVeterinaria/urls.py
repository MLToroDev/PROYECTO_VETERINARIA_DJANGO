from django.urls import path
from . import views

urlpatterns = [
    path('RegistrarPersona/', views.RegistrarPersona),

]