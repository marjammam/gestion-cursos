from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import DocenteViewSet, EstudianteViewSet, RegistroUsuarioView

router = DefaultRouter()
router.register(r'docentes', DocenteViewSet, basename='docente')
router.register(r'estudiantes', EstudianteViewSet, basename='estudiante')

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
] + router.urls