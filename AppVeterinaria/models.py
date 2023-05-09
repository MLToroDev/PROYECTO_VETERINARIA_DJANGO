from django.db import models


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    id_registro = models.ForeignKey('Registro', models.DO_NOTHING, db_column='id_registro')
    nombre_producto_cantidad = models.CharField(db_column='nombre_producto-cantidad', max_length=500)  # Field renamed to remove unsuitable characters.
    fecha = models.DateTimeField()
    valor = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'factura'


class HistorialClinico(models.Model):
    id_mascota = models.OneToOneField('Mascota', models.DO_NOTHING, db_column='id_mascota', primary_key=True)
    id_registro = models.ForeignKey('Registro', models.DO_NOTHING, db_column='id_registro')

    class Meta:
        managed = False
        db_table = 'historial_clinico'


class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    cedula_dueño = models.ForeignKey('Persona', models.DO_NOTHING, db_column='cedula_due±o')
    nombre_mascota = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    caracteristicas = models.CharField(max_length=50)
    peso = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'mascota'


class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    medicamento_dosis = models.CharField(db_column='medicamento-dosis', max_length=500)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'orden'


class Persona(models.Model):
    cedula_persona = models.CharField(primary_key=True, max_length=20)
    nombre_persona = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.CharField(max_length=3)
    id_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='id_rol')
    usuario = models.CharField(max_length=50, blank=True, null=True)
    contraseña = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persona'


class Registro(models.Model):
    fecha_registro = models.DateTimeField(db_column='Fecha_Registro', primary_key=True)  # Field name made lowercase.
    id_mascota = models.ForeignKey(Mascota, models.DO_NOTHING, db_column='ID_Mascota')  # Field name made lowercase.
    cedula_veterinario = models.ForeignKey(Persona, models.DO_NOTHING, db_column='Cedula_Veterinario')  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=500)  # Field name made lowercase.
    sintomatologia = models.CharField(db_column='Sintomatologia', max_length=500, blank=True, null=True)  # Field name made lowercase.
    diagnostico = models.CharField(db_column='Diagnostico', max_length=500)  # Field name made lowercase.
    procedimiento = models.CharField(db_column='Procedimiento', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detalle_procedimiento = models.CharField(db_column='Detalle_Procedimiento', max_length=500, blank=True, null=True)  # Field name made lowercase.
    historial_vacunacion = models.CharField(db_column='Historial_Vacunacion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    id_orden = models.ForeignKey(Orden, models.DO_NOTHING, db_column='ID_Orden', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'registro'


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    tipo_rol = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'rol'
