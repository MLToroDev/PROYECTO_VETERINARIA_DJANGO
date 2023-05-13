from django.contrib import admin;
from django.urls import path, include;
from AppVeterinaria import views;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('AppVeterinaria.urls')),
    path('', views.signin)
]
