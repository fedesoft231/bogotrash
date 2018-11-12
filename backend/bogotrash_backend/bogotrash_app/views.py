from django.shortcuts import render
from bogotrash_app.models import *

from rest_framework import generics
from bogotrash_app.serializers import *

from rest_framework.decorators import permission_classes
from bogotrash_app.permissions import IsPostOrIsAuthenticated


def principal(request):
    usuarios = Usuario.objects.all()
    return render(request, 'inicio.html', {'ok':usuarios})

class QuejaList(generics.ListCreateAPIView):
    serializer_class = QuejaSerializer
    queryset = Queja.objects.all()

class QuejaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuejaSerializer
    queryset = Queja.objects.all()

class CatalogoList(generics.ListCreateAPIView):
    serializer_class = CatalogoSerializer
    queryset = Catalogo.objects.all()
    
class CatalogoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CatalogoSerializer
    queryset = Catalogo.objects.all()

class CentroList(generics.ListCreateAPIView):
    serializer_class = CentroSerializer
    queryset = Centro.objects.all()
    
class CentroDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CentroSerializer
    queryset = Centro.objects.all()

class DesechoList(generics.ListCreateAPIView):
    serializer_class = DesechoSerializer
    queryset = Desecho.objects.all()

class DesechoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DesechoSerializer
    queryset = Desecho.objects.all()

class TipoDesechoList(generics.ListCreateAPIView):
    serializer_class = TipoDesechoSerializer
    queryset = TipoDesecho.objects.all()
    
class TipoDesechoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TipoDesechoSerializer
    queryset = TipoDesecho.objects.all()

@permission_classes((IsPostOrIsAuthenticated, ))
class UsuarioList(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

# Create your views here.