from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Curso, Inscripcion
from .serializers import CursoSerializer, InscripcionSerializer
from rest_framework import filters

class SoloAdminEscribeOtrosLeen(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user.tipo_usuario == 'ADMINISTRADOR'


class CursoViewSet(viewsets.ModelViewSet):
    serializer_class = CursoSerializer
    permission_classes = [SoloAdminEscribeOtrosLeen]
    filterset_fields = ['docente', 'activo']
    search_fields = ['nombre', 'codigo']

    def get_queryset(self):
        usuario = self.request.user
        queryset = Curso.objects.select_related('docente__usuario').all()

        if usuario.tipo_usuario == 'ADMINISTRADOR':
            return queryset
        elif usuario.tipo_usuario == 'DOCENTE':
            return queryset.filter(docente__usuario=usuario)
        elif usuario.tipo_usuario == 'ESTUDIANTE':
            return queryset.filter(inscripciones__estudiante__usuario=usuario).distinct()
        return queryset.none()


class InscripcionViewSet(viewsets.ModelViewSet):
    serializer_class = InscripcionSerializer
    permission_classes = [SoloAdminEscribeOtrosLeen]
    filterset_fields = ['estudiante', 'curso']

    def get_queryset(self):
        usuario = self.request.user
        queryset = Inscripcion.objects.select_related('estudiante__usuario', 'curso').all()

        if usuario.tipo_usuario == 'ADMINISTRADOR':
            return queryset
        elif usuario.tipo_usuario == 'ESTUDIANTE':
            return queryset.filter(estudiante__usuario=usuario)
        elif usuario.tipo_usuario == 'DOCENTE':
            return queryset.filter(curso__docente__usuario=usuario)
        return queryset.none()