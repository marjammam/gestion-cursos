
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    ADMINISTRADOR = 'ADMINISTRADOR'
    DOCENTE = 'DOCENTE'
    ESTUDIANTE = 'ESTUDIANTE'

    TIPO_USUARIO_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (DOCENTE, 'Docente'),
        (ESTUDIANTE, 'Estudiante'),
    ]

    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

    def __str__(self):
        return self.username

class Docente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='docente')
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.username


class Estudiante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='estudiante')
    codigo_estudiante = models.CharField(max_length=20, unique=True)
    carrera = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.username