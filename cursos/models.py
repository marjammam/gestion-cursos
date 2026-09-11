
# Create your models here.
from django.db import models
from usuarios.models import Docente
from usuarios.models import Estudiante


class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(blank=True)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='cursos')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'curso')  # evita inscripciones duplicadas

    def __str__(self):
        return f"{self.estudiante} - {self.curso}"