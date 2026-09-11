from rest_framework import serializers
from .models import Curso, Inscripcion


class CursoSerializer(serializers.ModelSerializer):
    docente_nombre = serializers.CharField(source='docente.usuario.username', read_only=True)

    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'codigo', 'descripcion', 'docente', 'docente_nombre', 'activo']


class InscripcionSerializer(serializers.ModelSerializer):
    estudiante_nombre = serializers.CharField(source='estudiante.usuario.username', read_only=True)
    curso_nombre = serializers.CharField(source='curso.nombre', read_only=True)

    class Meta:
        model = Inscripcion
        fields = ['id', 'estudiante', 'estudiante_nombre', 'curso', 'curso_nombre', 'fecha_inscripcion']