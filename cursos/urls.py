from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, InscripcionViewSet

router = DefaultRouter()
router.register(r'cursos', CursoViewSet, basename='curso')
router.register(r'inscripciones', InscripcionViewSet, basename='inscripcion')

urlpatterns = router.urls