**Sistema de Gestión de Cursos** 

**Descripción**
Aplicación backend desarrollada con Django y Django REST Framework para la gestión de cursos, docentes, estudiantes e inscripciones. El sistema maneja tres tipos de usuario (Administrador, Docente, Estudiante), cada uno con permisos diferenciados, y utiliza autenticación mediante JWT.
Funcionalidades principales:
Gestión de usuarios, docentes y estudiantes.
CRUD de cursos e inscripciones.
Permisos por rol de usuario.
Filtros, búsqueda y paginación en los endpoints principales.
Documentación interactiva de la API con Swagger.
**Tecnologías utilizadas**
Python
Django
Django REST Framework
PostgreSQL
Simple JWT
drf-yasg (Swagger/OpenAPI)
django-filter
**Instalación**
Clonar el repositorio:
```bash
git clone <https://github.com/marjammam/gestion-cursos.git>
cd gestion-cursos
```
Crear el entorno virtual:
```bash
python -m venv venv
```
Activar el entorno virtual:
Windows:
```bash
venv\Scripts\activate
```
Linux/Mac:
```bash
source venv/bin/activate
```
Instalar dependencias:
```bash
pip install -r requirements.txt
```
**Configuración de base de datos**
El proyecto utiliza PostgreSQL. Antes de ejecutar el proyecto:
Crea una base de datos en PostgreSQL (por ejemplo, con pgAdmin):
```sql
CREATE DATABASE gestion_cursos_db;
```
Copia el archivo `.env.example` a un nuevo archivo `.env`:
```bash
cp .env.example .env
```
(en Windows puedes copiarlo manualmente o usar `copy .env.example .env`)
Edita `.env` con tus credenciales reales de PostgreSQL:
```
SECRET_KEY=tu-clave-secreta
DEBUG=True
DB_NAME=gestion_cursos_db
DB_USER=postgres
DB_PASSWORD=tu_password
DB_HOST=127.0.0.1
DB_PORT=5432
```
> El archivo `.env` no se sube al repositorio (está excluido en `.gitignore`). Para producción, cambia `DEBUG=False`.
Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```
Creación del superusuario
```bash
python manage.py createsuperuser
```
**Ejecución***
```bash
python manage.py runserver
```
La aplicación estará disponible en `http://127.0.0.1:5050/` (o el puerto que definas).
Documentación de la API
Con el servidor corriendo, accede a:
Swagger: `http://127.0.0.1:5050/api/docs/`
Redoc: `http://127.0.0.1:5050/redoc/`
Autenticación JWT
Login (obtener tokens): `POST /api/token/`
```json
{
  "username": "tu_usuario",
  "password": "tu_contraseña"
}
```
Refrescar token: `POST /api/token/refresh/`
```json
{
  "refresh": "tu_refresh_token"
}
```
Los endpoints protegidos requieren el header:
```
Authorization: Bearer <access_token>
```
**Tipos de usuario y permisos**
**Rol	Permisos**
Administrador	Gestiona docentes, estudiantes, cursos e inscripciones (CRUD completo)
Docente	Consulta sus cursos asignados y los estudiantes inscritos en ellos
Estudiante	Consulta sus cursos inscritos y su información personal
###Endpoints principales
Método	Endpoint	Descripción
POST	`/api/registro/`	Registro de nuevo usuario
POST	`/api/token/`	Login (obtener access y refresh token)
POST	`/api/token/refresh/`	Renovar access token
GET/POST	`/api/docentes/`	Listar / crear docentes (solo Administrador)
GET/PUT/DELETE	`/api/docentes/{id}/`	Detalle, actualizar o eliminar un docente
GET/POST	`/api/estudiantes/`	Listar / crear estudiantes (solo Administrador)
GET/PUT/DELETE	`/api/estudiantes/{id}/`	Detalle, actualizar o eliminar un estudiante
GET/POST	`/api/cursos/`	Listar cursos (según rol) / crear curso (solo Administrador)
GET/PUT/DELETE	`/api/cursos/{id}/`	Detalle, actualizar o eliminar un curso
GET/POST	`/api/inscripciones/`	Listar inscripciones (según rol) / crear inscripción (solo Administrador)
GET/PUT/DELETE	`/api/inscripciones/{id}/`	Detalle, actualizar o eliminar una inscripción
Filtros y búsqueda
`GET /api/cursos/?docente={id}` — cursos de un docente específico
`GET /api/cursos/?activo=true` — solo cursos activos
`GET /api/cursos/?search=texto` — búsqueda por nombre o código de curso
`GET /api/inscripciones/?estudiante={id}` — inscripciones de un estudiante específico
`GET /api/estudiantes/?search=texto` — búsqueda por nombre de estudiante
**Paginación**
Los endpoints principales devuelven resultados paginados (10 por página por defecto).
Optimización de consultas
Se utiliza `select_related()` en los querysets de Docente, Estudiante, Curso e Inscripción para optimizar las consultas relacionadas y evitar el problema N+1.
