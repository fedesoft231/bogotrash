from django.db import models
from django.contrib.auth.models import User


class Centro(models.Model):
    nombre = models.CharField(max_length = 50)
    ubicacion = models.CharField(max_length = 100)

class TipoDesecho(models.Model):
    nombre = models.CharField(max_length = 100)
    centro = models.ManyToManyField(Centro)

class Desecho(models.Model):
    nombre = models.CharField(max_length = 100)
    tipo = models.ForeignKey(TipoDesecho, on_delete=models.CASCADE)
    info = models.TextField()
    
class Catalogo(models.Model):
    desecho = models.ManyToManyField(Desecho)
 
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    cedula = models.IntegerField()
    catalogo = models.ManyToManyField(Catalogo, blank=True, null=True)
    def __str__(self):
        return self.apellido + " " + self.nombre

class Queja(models.Model):
    descripcion = models.CharField(max_length = 500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    foto = models.CharField(max_length = 100, blank=True, null=True)
    ubicacion = models.CharField(max_length = 100)
    user = models.ForeignKey(Usuario, on_delete = models.CASCADE)