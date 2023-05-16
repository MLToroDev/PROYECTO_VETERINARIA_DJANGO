from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('', views.bienvenida, name='bienvenida'),
    path('menu_principal/', views.menuPl)
    #path('logout/', LogoutView.as_view(), name='logout')
]