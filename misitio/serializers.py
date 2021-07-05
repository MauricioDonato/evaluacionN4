from django.contrib.auth.models import User, Group
from rest_framework import serializers
from pasteleria.models import Cliente, Comuna, Producto

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'rut', 'nombre_cli', 'apellido_cli', 'fecha_nac', 'correo', 'direccion', 'comuna' ,'contrasena', 'contrasena_val']

class ComunaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comuna
        fields = ['id', 'nombre_c']
class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre_pro', 'precio_pro']
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']