# ClassroomHub

## 1. Descripción del proyecto

ClassroomHub es una aplicación web desarrollada con Django como parte de un proceso de aprendizaje sobre desarrollo web con Python. Su propósito es administrar y consultar recursos educativos organizados por categorías, implementando funcionalidades de autenticación, autorización y control de acceso.

El proyecto permite consultar recursos, visualizar categorías, gestionar la disponibilidad de los recursos y acceder a funcionalidades privadas mediante cuentas de usuario.

## 2. Tecnologías utilizadas

- Python 3.14.
- Django 6.1.3.
- HTML.
- SQLite o MySQL/MariaDB, según la configuración del proyecto.
- ORM de Django.
- Sistema de autenticación integrado de Django.
- Git y GitHub.

## 3. Funcionalidades implementadas

- Página principal de ClassroomHub.
- Catálogo de recursos educativos.
- Consulta de recursos disponibles.
- Organización de recursos mediante categorías.
- Sistema de registro de usuarios.
- Inicio y cierre de sesión.
- Autenticación mediante el sistema de usuarios de Django.
- Protección de vistas mediante `login_required`.
- Control de permisos mediante el sistema de autorización de Django.
- Resumen privado de recursos.
- Pruebas automatizadas para comprobar el acceso de usuarios autenticados y visitantes anónimos.

## 4. Estructura del proyecto

```text
classroom-hub/
│
├── .venv/
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── pages/
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_resource_resource_type.py
│   │   
│   ├── templates/
│   │   ├── pages/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── faq.html
│   │   ├── contact.html
│   │   ├── resources.html
│   │   ├── signup.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── dashboard_summary.html
│   │   └── review.html
│   │   
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
├── README.md
└── requirements.txt
```

La estructura puede incluir otras plantillas y archivos correspondientes a las funcionalidades anteriores del laboratorio.

## 5. Requisitos previos

Antes de instalar el proyecto se necesita:

- Python 3.14 instalado.
- Git instalado.
- Un gestor de base de datos compatible con la configuración del proyecto.
- Un editor de código, como Visual Studio Code.

## 6. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta:

```bash
cd classroom-hub
```

## 7. Crear y activar el entorno virtual

En Windows:

```bash
python -m venv .venv
```

Activar el entorno virtual:

```bash
.venv\Scripts\activate
```

## 8. Instalar dependencias

Actualizar pip:

```bash
python -m pip install --upgrade pip
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## 9. Configuración de variables de entorno

Crear un archivo `.env` en la raíz del proyecto.

Este archivo debe contener las variables utilizadas por `config/settings.py`.

Ejemplo para una configuración MySQL/MariaDB:

```env
DB_NAME=classroom_hub
DB_USER=usuario_base_datos
DB_PASSWORD=contraseña_base_datos
DB_HOST=localhost
DB_PORT=3306
```

Los nombres de las variables deben coincidir con los utilizados en el proyecto.

No se deben publicar contraseñas, claves secretas ni información privada en GitHub.

## 10. Crear la base de datos

Si se utiliza MySQL o MariaDB, ingresar al gestor de bases de datos y ejecutar:

```sql
CREATE DATABASE classroom_hub
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

Configurar la conexión en el archivo de variables de entorno y verificar que Django pueda conectarse correctamente.

Si el proyecto utiliza SQLite, Django crea el archivo de base de datos al ejecutar las migraciones y no es necesario crear previamente una base mediante SQL.

## 11. Aplicar migraciones

Verificar las migraciones pendientes:

```bash
python manage.py showmigrations
```

Crear migraciones cuando existan cambios en los modelos:

```bash
python manage.py makemigrations
```

Aplicar las migraciones:

```bash
python manage.py migrate
```

Los archivos de migración deben versionarse en GitHub. No se debe versionar el contenido real de la base de datos.

## 12. Crear un superusuario

Para acceder al panel administrativo de Django:

```bash
python manage.py createsuperuser
```

Ingresar el nombre de usuario, correo electrónico y contraseña solicitados.

## 13. Ejecutar el servidor

Iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## 14. Resumen privado de recursos

Se implementó una vista de solo lectura en:

```text
/dashboard/summary/
```

Esta funcionalidad permite consultar:

- Número total de recursos registrados.
- Número de recursos disponibles.

La información se obtiene mediante consultas al ORM de Django utilizando `count()` y `filter()`.

La vista está protegida mediante `@login_required`, por lo que los visitantes anónimos son redirigidos al inicio de sesión. No exige el permiso `view_resource`, ya que el objetivo del reto es permitir que cualquier usuario autenticado consulte las estadísticas.

## 15. Seguridad y control de acceso

El proyecto utiliza el sistema de autenticación integrado de Django para gestionar las cuentas de usuario y las sesiones.

Se implementan mecanismos como:

- Registro de usuarios.
- Inicio y cierre de sesión.
- Almacenamiento seguro de contraseñas mediante el sistema de Django.
- Protección CSRF en formularios.
- Restricción de acceso a vistas privadas.
- Comprobación de permisos desde las vistas.
- Diferenciación entre autenticación y autorización.

## 16. Ejecutar las pruebas

Verificar la configuración del proyecto:

```bash
python manage.py check
```

Ejecutar las pruebas de la aplicación:

```bash
python manage.py test pages
```

Ejecutar específicamente las pruebas del resumen privado:

```bash
python manage.py test pages.tests.DashboardSummaryTests
```

Las pruebas comprueban el comportamiento de los usuarios anónimos y autenticados, así como los valores de los recursos registrados.

## 17. Versionamiento con Git

Consultar los cambios:

```bash
git status
```

Agregar los archivos:

```bash
git add .
```

Crear un commit:

```bash
git commit -m "feat: add private resource summary dashboard"
```

Subir los cambios a la rama de trabajo:

```bash
git push origin nombre-de-la-rama
```

Se deben versionar el código fuente, las plantillas, las pruebas, los archivos de configuración compartibles y las migraciones.

No se deben subir:

- El entorno virtual `.venv/`.
- El archivo `.env`.
- Contraseñas o claves secretas.
- Bases de datos locales con información real.
- Archivos temporales o cachés de Python.

