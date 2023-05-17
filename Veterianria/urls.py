from django.contrib import admin;
from django.urls import path, include;
from AppVeterinaria import views;
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', views.bienvenida, name='bienvenida'),
    path('admin/', admin.site.urls),
    path('inicio/', include('AppVeterinaria.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
