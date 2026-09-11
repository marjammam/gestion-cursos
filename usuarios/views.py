from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Docente, Estudiante
from .serializers import DocenteSerializer, EstudianteSerializer, UsuarioSerializer
from .permissions import EsAdministrador
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.select_related('usuario').all()
    serializer_class = DocenteSerializer
    permission_classes = [EsAdministrador]

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.select_related('usuario').all()
    serializer_class = EstudianteSerializer
    permission_classes = [EsAdministrador]
    search_fields = ['usuario__username', 'usuario__first_name', 'usuario__last_name']

class RegistroUsuarioView(APIView):
    permission_classes = []  # público, para poder crear la primera cuenta

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Usuario creado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)