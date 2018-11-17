from django.db import models
from django.contrib.auth.models import User
from django_google_maps import fields as map_fields

class TipoDesecho(models.Model):
    nombre = models.CharField(max_length = 100)

class Centro(models.Model):
    nombre = models.CharField(max_length = 50)
    ubicacion = models.CharField(max_length = 100)
    tipo_desecho = models.ManyToManyField(TipoDesecho)

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
    foto = models.ImageField(upload_to='img/fotosapp/', blank=True, null=True)
    dirección = map_fields.AddressField(max_length=200, verbose_name='Dirección', blank=True, null=True)
    geolocacion = map_fields.GeoLocationField(max_length=100, verbose_name='Coordenadas', blank=True, null=True)
    ubicacion = models.CharField(max_length = 100)
    user = models.ForeignKey(Usuario, on_delete = models.CASCADE)
