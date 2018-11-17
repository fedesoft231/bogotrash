from rest_framework import serializers
from bogotrash_app.models import Usuario, Queja, Catalogo, Centro, Desecho, TipoDesecho
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField


class QuejaSerializer(serializers.ModelSerializer):
    foto = Base64ImageField()
    class Meta:
       model = Queja
       fields = ('descripcion', 'fecha_creacion', 'foto', 'ubicacion', 'user')

class CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
       model = Catalogo
       fields = ('desecho', )

class CentroSerializer(serializers.ModelSerializer):
    class Meta:
       model = Centro
       fields = ('nombre', 'ubicacion')

class DesechoSerializer(serializers.ModelSerializer):
    class Meta:
       model = Desecho
       fields = ('nombre', 'tipo', 'info')

class TipoDesechoSerializer(serializers.ModelSerializer):
    class Meta:
       model = TipoDesecho
       fields = ('nombre', 'centro')

class UsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, source="user.username")
    password = serializers.CharField(write_only=True, source="user.password")
    nombre = serializers.CharField(required=False)
    apellido = serializers.CharField(required=False)
    correo = serializers.CharField(required=False)
    cedula = serializers.DateField(required=False)
    catalogo = serializers.CharField(required=False)
    #category_name = serializers.RelatedField(source='category', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'nombre', 'apellido', 'correo', 'cedula', 'catalogo')

    def create(self, validated_data, instance=None):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        user.save()
        Usuario.objects.update_or_create(user=user,**validated_data)
        usuario = Usuario.objects.get(user=user)
        
        return usuario