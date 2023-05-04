from django.db import models
from datetime import datetime

class Persona(models.Model):
    Cedula = models.CharField(max_length=20, primary_key=True)
    Nombre_Persona = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Edad = models.IntegerField()
    Id_Rol = models.CharField(max_length=12)
    Usuario = models.CharField(max_length=20, null=True)
    Contrasena = models.CharField(max_length=20, null=True)

class Mascota(models.Model):
    Id_Mascota = models.AutoField(primary_key=True, unique=True)
    Nombre_Mascota = models.CharField(max_length=50)
    Especie = models.CharField(max_length=20)
    Raza = models.CharField(max_length=50)
    Caracteristicas = models.CharField(max_length=100)
    Peso = models.DecimalField(max_digits=5, decimal_places=2)

class Registro(models.Model):
    Fecha = models.CharField(max_length=20, primary_key=True)
    Id_Mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    Motivo = models.CharField(max_length=500)
    Sintomatologia = models.CharField(max_length=500, null=True)
    Diagnostico = models.CharField(max_length=500)
    Procedimiento = models.CharField(max_length=100, null=True)
    Detalle_Procedimiento = models.CharField(max_length=500, null=True)
    Id_Orden = models.IntegerField(null=True)
    Historial_Vacunacion = models.CharField(max_length=500, null=True)
    Medicamento_Alergico = models.CharField(max_length=100, null=True)
    Anulacion_Orden = models.BooleanField(null=True)
    Id_Factura = models.AutoField(null=True)

class HistorialClinico(models.Model):
    Id_Mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    Id_Registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    Id_Historial_Clinica = models.AutoField(null=True)

class Orden(models.Model):
    Id_Orden = models.AutoField(primary_key=True)
    Medicamento = models.CharField(max_length=200, null=True)
    Dosis = models.CharField(max_length=50, null=True)

class Rol(models.Model):
    Id_Rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    Admin = models.IntegerField(null=True)
    Doct = models.AutoField(null=True)

class Factura(models.Model):
    Id_Factura = models.AutoField(primary_key=True)
    Id_Registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    Id_Orden = models.ForeignKey(Orden, null=True, on_delete=models.CASCADE)
    Nombre_Producto = models.CharField(max_length=100, null=True)
    Cantidad = models.IntegerField(null=True)
    Valor = models.FloatField()
    Fecha = models.DateTimeField(default=datetime.now)
