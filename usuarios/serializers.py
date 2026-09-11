from rest_framework import serializers
from .models import Usuario, Docente, Estudiante


class DocenteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = Docente
        fields = ['id', 'usuario', 'username', 'especialidad']


class EstudianteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = Estudiante
        fields = ['id', 'usuario', 'username', 'codigo_estudiante', 'carrera']

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'tipo_usuario']

    def create(self, validated_data):
        password = validated_data.pop('password')
        usuario = Usuario(**validated_data)
        usuario.set_password(password)
        usuario.save()
        return usuario