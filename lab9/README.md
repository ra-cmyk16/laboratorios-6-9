# ClassroomHub

## 1. Descripción del proyecto

ClassroomHub es una aplicación web desarrollada con Django como parte de los laboratorios de aprendizaje de desarrollo web con Python. Su propósito es organizar recursos educativos mediante un catálogo que permite consultar, registrar, actualizar y eliminar materiales de aprendizaje.

Durante los laboratorios se implementaron funcionalidades relacionadas con el manejo de rutas, vistas, plantillas, modelos, bases de datos, autenticación, permisos, formularios y operaciones CRUD.

## 2. Tecnologías utilizadas

- **Python:** 3.15.0 (entorno de desarrollo utilizado).
- **Django:** framework principal del proyecto.
- **MariaDB:** sistema de gestión de bases de datos.
- **HTML:** estructura de las páginas.
- **CSS:** presentación y estilos.
- **Git y GitHub:** control de versiones y almacenamiento del código.

## 3. Funcionalidades implementadas

### Laboratorios 6 y 7: Fundamentos de Django

- Configuración inicial del proyecto Django.
- Creación de la aplicación `pages`.
- Implementación de modelos `Category` y `Resource`.
- Configuración de rutas y vistas.
- Creación de plantillas HTML.
- Implementación del catálogo de recursos.
- Relación entre categorías y recursos.
- Configuración de migraciones y acceso a la base de datos.

### Laboratorio 8: Autenticación y permisos

- Registro de usuarios.
- Inicio y cierre de sesión.
- Protección de páginas mediante `login_required`.
- Implementación de un panel privado para usuarios autenticados.
- Contador de visitas utilizando sesiones.
- Creación de un resumen de recursos.
- Configuración de grupos y permisos para revisar el catálogo.

### Laboratorio 9: Formularios y CRUD

- Creación de `ResourceForm` mediante `forms.ModelForm`.
- Validación personalizada de los títulos de los recursos.
- Consulta pública del detalle de cada recurso.
- Protección del formulario de creación para usuarios autenticados.
- Implementación de operaciones de creación, consulta, actualización y eliminación de recursos.
- Control de acceso mediante autenticación y permisos.
- Implementación de una búsqueda pública por título utilizando `title__icontains`.
- Pruebas automatizadas para comprobar formularios, operaciones CRUD, permisos y búsqueda.

## 4. Requisitos previos

Para ejecutar el proyecto se necesita:

- Python instalado.
- Django instalado mediante las dependencias del proyecto.
- MariaDB instalado y funcionando.
- Git instalado.
- Un editor de código, como Visual Studio Code.

## 5. Clonar el repositorio

Clonar el repositorio desde GitHub:

```bash
git clone https://github.com/ra-cmyk16/laboratorios-6-9.git
```

Ingresar a la carpeta del laboratorio 9:

```bash
cd laboratorios-6-9/lab9
```

## 6. Crear y activar el entorno virtual

Crear el entorno virtual:

```bash
python -m venv .venv
```

Activarlo en Windows:

```bash
.venv\Scripts\activate
```

## 7. Instalar dependencias

Actualizar pip:

```bash
python -m pip install --upgrade pip
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## 8. Configuración de la base de datos

El proyecto utiliza MariaDB para almacenar la información de las categorías y los recursos.

Primero, inicia el servicio de MariaDB y crea la base de datos:

```sql
CREATE DATABASE classroom_hub
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

Configura las variables de conexión en un archivo `.env` ubicado en la raíz del proyecto.

Ejemplo de configuración:

```env
DB_NAME=classroom_hub
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=3306
```

Los valores deben corresponder a la configuración de MariaDB de cada entorno. No se deben publicar contraseñas ni credenciales reales.

Verifica que `config/settings.py` lea estas variables de entorno y utilice el motor de base de datos MySQL/MariaDB de Django.

## 9. Ejecutar las migraciones

Después de configurar la base de datos, ejecutar:

```bash
python manage.py makemigrations
```

Aplicar las migraciones:

```bash
python manage.py migrate
```

Las migraciones permiten crear y actualizar las tablas correspondientes a los modelos del proyecto.

## 10. Crear un superusuario

Para acceder al administrador de Django, ejecutar:

```bash
python manage.py createsuperuser
```

Completar los datos solicitados por la terminal.

El administrador permite gestionar usuarios, categorías y recursos según los modelos y registros administrativos configurados.

## 11. Ejecutar el servidor

Iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## 12. Rutas principales

| Ruta | Funcionalidad |
|---|---|
| `/` | Página principal. |
| `/resources/` | Catálogo público de recursos. |
| `/resources/available/` | Recursos disponibles. |
| `/resources/review/` | Revisión del catálogo con permisos. |
| `/resources/create/` | Formulario protegido para crear recursos. |
| `/resources/<id>/` | Detalle de un recurso. |
| `/about/` | Información del proyecto. |
| `/faq/` | Preguntas frecuentes. |
| `/contact/` | Información de contacto. |
| `/accounts/signup/` | Registro de usuarios. |
| `/accounts/login/` | Inicio de sesión. |
| `/accounts/logout/` | Cierre de sesión. |
| `/dashboard/` | Panel privado del usuario. |
| `/dashboard/summary/` | Resumen de recursos para usuarios autenticados. |

Las rutas de actualización y eliminación también requieren los controles de acceso correspondientes.

## 13. Formularios y validaciones

El proyecto utiliza `ResourceForm`, construido con `forms.ModelForm`, para facilitar la creación y modificación de recursos.

Los campos del formulario se declaran explícitamente para controlar qué información puede enviar el usuario.

También se implementa una validación personalizada que exige que el título del recurso tenga al menos tres caracteres.

Los formularios utilizan el método POST y protección CSRF para procesar los datos de manera segura.

## 14. Autenticación y permisos

ClassroomHub utiliza el sistema de autenticación integrado de Django.

Las páginas privadas requieren que el usuario haya iniciado sesión. Además, algunas operaciones necesitan permisos específicos.

Se utilizan grupos para organizar los permisos de los usuarios:

- **Catalog reviewers:** usuarios encargados de revisar los recursos.
- **Catalog editors:** usuarios con permisos de edición del catálogo.

La visibilidad de los enlaces en las plantillas no reemplaza la comprobación de permisos realizada en las vistas.

## 15. Búsqueda de recursos

El catálogo incorpora una búsqueda sencilla mediante el método GET.

El usuario puede escribir una palabra o parte del título para encontrar recursos que coincidan con el término ingresado.

La consulta utiliza:

```python
Resource.objects.filter(
    title__icontains=query
)
```

Esta funcionalidad es pública y de solo lectura, por lo que no modifica ni elimina registros de la base de datos.

## 16. Ejecutar las pruebas

Para comprobar el funcionamiento de la aplicación, ejecutar:

```bash
python manage.py check
```

Para ejecutar las pruebas de la aplicación `pages`:

```bash
python manage.py test pages
```

Las pruebas permiten verificar:

- Funcionamiento de las páginas y rutas.
- Consulta y visualización de recursos.
- Relación entre categorías y recursos.
- Formularios y validaciones.
- Creación, actualización y eliminación.
- Autenticación y permisos.
- Funcionamiento de la búsqueda.
- Respuestas HTTP y manejo de recursos inexistentes.

## 17. Estructura general del proyecto

```text
lab9/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── pages/
│   ├── migrations/
│   ├── templates/
│   │   └── pages/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── resources.html
│   │       ├── resource_detail.html
│   │       ├── resource_form.html
│   │       ├── dashboard.html
│   │       ├── dashboard_summary.html
│   │       ├── review.html
│   │       ├── login.html
│   │       ├── signup.html
│   │       ├── about.html
│   │       └── faq.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

La estructura representa los archivos principales del proyecto. Pueden existir archivos adicionales según las funcionalidades y plantillas implementadas.

## 18. Control de versiones y archivos que no deben publicarse

El repositorio debe contener el código fuente, las plantillas, los archivos de configuración necesarios y las migraciones de Django.

Se deben versionar las migraciones para conservar el historial de cambios de los modelos.

No se deben publicar:

- El archivo `.env` con credenciales reales.
- Contraseñas o datos privados.
- Bases de datos locales con información real.
- El entorno virtual `.venv/`.
- Archivos temporales o cachés de Python.

Se recomienda incluir estas exclusiones en `.gitignore`:

```gitignore
.venv/
__pycache__/
*.py[cod]
.env
db.sqlite3
```

Si se utiliza otra base de datos local, también debe excluirse su archivo correspondiente.