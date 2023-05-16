
from django.contrib import admin;
from django.urls import path, include;
from AppVeterinaria import views;





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppVeterinaria.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
