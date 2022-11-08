from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Empleado(models.Model):
    id_empleado= models.AutoField(primary_key=True)
    nombre_completo= models.CharField(max_length=40,verbose_name='NOMBRE COMPLETO')
    rut= models.IntegerField(verbose_name='RUT')
    dv_rut= models.IntegerField(verbose_name='DIGITO VERIFICADOR')
    correo = models.EmailField(verbose_name='MAIL')


    def __str__(self):
        return self.nombre_completo

class Servicio(models.Model):
    id_servicio= models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=30, verbose_name='NOMBRE SERVICIO')
    tipo = models.CharField(max_length=30, null=True, verbose_name='TIPO')
    precio = models.IntegerField(null=True, verbose_name='PRECIO')
    usuario = models.ForeignKey(User, null= True, on_delete=models.PROTECT, related_name='USUARIO')

    def __str__(self):
        return self.nombre_servicio

opc_hora = [
    [0, "8:00hrs. - 8:59hrs."],
    [1, "9:00hrs. - 9:59hrs."],
    [2, "10:00hrs. - 10:59hrs."],
    [3, "11:00hrs. - 11:59hrs."],
    [4, "12:00hrs. - 12:59hrs."],
    [5, "13:00hrs. - 13:59hrs."],
    [6, "14:00hrs. - 14:59hrs."]
]

class Cliente(models.Model):
    id_cliente= models.AutoField(primary_key=True)
    nombre_completo= models.CharField(max_length=40,verbose_name='NOMBRE COMPLETO')
    rut= models.IntegerField(verbose_name='RUT')
    dv_rut= models.IntegerField(verbose_name='DIGITO VERIFICADOR')
    correo = models.EmailField(verbose_name='MAIL')

    def __str__(self):
        return self.nombre_completo

class Cuenta(models.Model):
    id_cuenta =  models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30, verbose_name='USUARIO')
    correo = models.EmailField(verbose_name='MAIL')
    password = models.CharField(max_length=20, verbose_name='PASSWORD')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario



class Reserva(models.Model):
    id_reserva= models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add= False, auto_now= False, blank = True, null=True, verbose_name='FECHA')
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT, verbose_name='SERVICIO')
    hora = models.IntegerField(choices = opc_hora, verbose_name='HORA')
    confirmada = models.BooleanField(default=False)
   
    

    def __str__(self):
        return self.fecha

