# ClassroomHub

## Descripción del proyecto

ClassroomHub es una aplicación web desarrollada con Python y Django como ejercicio de aprendizaje. Permite consultar recursos educativos organizados por categorías y administrar su información mediante Django Admin.

## Funcionalidades

- **Página de inicio:** muestra un mensaje de bienvenida.
- **Página de recursos:** presenta los recursos educativos registrados en la base de datos.
- **Consulta de disponibilidad:** permite consultar únicamente los recursos disponibles.
- **Página Acerca de:** contiene información sobre el propósito del proyecto.
- **Página FAQ:** presenta preguntas frecuentes.
- **Página de contacto:** muestra información de contacto.
- **Django Admin:** permite administrar categorías y recursos.
- **Relaciones entre modelos:** cada recurso pertenece a una categoría.

## Tecnologías utilizadas

- Python 3.12 o superior.
- Django.
- MariaDB.
- HTML.
- Git y GitHub.

## Requisitos previos

Antes de instalar el proyecto, se necesita:

- Tener Python instalado.
- Tener MariaDB instalado y funcionando.
- Tener Git instalado.
- Contar con una terminal para ejecutar los comandos.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/ra-cmyk16/laboratorios-6-9.git
```

Ingresar a la carpeta del proyecto:

```bash
cd laboratorios-6-9
```

Si el laboratorio se encuentra dentro de una subcarpeta, ingresar también a ella.

### 2. Crear y activar el entorno virtual

En Windows:

```bash
python -m venv .venv
```

Activar el entorno:

```bash
.venv\Scripts\activate
```

### 3. Instalar las dependencias

Actualizar pip:

```bash
python -m pip install --upgrade pip
```

Instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## Configuración de la base de datos

### 4. Crear la base de datos en MariaDB

Ingresar a MariaDB y ejecutar:

```sql
CREATE DATABASE classroom_hub
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

Crear una cuenta para la aplicación:

```sql
CREATE USER 'classroomhub_user'@'localhost'
IDENTIFIED BY 'CAMBIAR_POR_UNA_CLAVE_SEGURA';
```

Dar permisos sobre la base de datos:

```sql
GRANT ALL PRIVILEGES ON classroom_hub.*
TO 'classroomhub_user'@'localhost';

FLUSH PRIVILEGES;
```

La cuenta SQL permite que Django se conecte a MariaDB. No es el mismo usuario que se utiliza para ingresar a Django Admin.

### 5. Configurar las variables de entorno

Crear un archivo llamado `.env` en la carpeta principal del proyecto.

Agregar la configuración de conexión:

```env
DB_NAME=classroom_hub
DB_USER=classroomhub_user
DB_PASSWORD=CAMBIAR_POR_LA_CLAVE_CONFIGURADA
DB_HOST=localhost
DB_PORT=3306
```

El archivo `.env` contiene información privada y no debe subirse a GitHub.

También se debe mantener un archivo `.env.example` con los nombres de las variables y valores de ejemplo, sin contraseñas reales:

```env
DB_NAME=classroom_hub
DB_USER=classroomhub_user
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

**Importante:** los nombres de las variables deben coincidir con los que utiliza `config/settings.py` para leer la configuración.

## Migraciones

### 6. Crear y aplicar las migraciones

Crear los archivos de migración a partir de los modelos:

```bash
python manage.py makemigrations
```

Aplicar las migraciones a la base de datos:

```bash
python manage.py migrate
```

Los archivos de migración deben guardarse en Git porque permiten reconstruir la estructura de la base de datos.

No se deben subir las contraseñas, los datos reales de la base de datos ni copias de seguridad con información privada.

## Crear el superusuario

### 7. Crear una cuenta de administrador

Ejecutar:

```bash
python manage.py createsuperuser
```

Ingresar el nombre de usuario, correo electrónico y contraseña solicitados.

Esta cuenta permite acceder al panel administrativo de Django.

## Ejecución del proyecto

### 8. Iniciar el servidor

Ejecutar:

```bash
python manage.py runserver
```

Abrir el navegador en:

http://127.0.0.1:8000/

Para consultar los recursos:

http://127.0.0.1:8000/resources/

Para consultar los recursos disponibles:

http://127.0.0.1:8000/resources/available/

Para ingresar al panel administrativo:

http://127.0.0.1:8000/admin/

## Ejecución de pruebas

### 9. Verificar la configuración

```bash
python manage.py check
```

### 10. Ejecutar las pruebas automatizadas

```bash
python manage.py test pages
```

Las pruebas permiten comprobar el funcionamiento de las vistas, las consultas y las funcionalidades de la aplicación.

## Estructura del proyecto

- `config/`: contiene la configuración principal del proyecto Django.
- `pages/`: contiene los modelos, vistas, rutas, pruebas y plantillas.
- `pages/migrations/`: contiene los archivos de migración de los modelos.
- `requirements.txt`: contiene las dependencias del proyecto.
- `.env`: contiene las variables privadas de configuración.
- `.env.example`: muestra las variables necesarias para configurar el proyecto.
- `.gitignore`: indica qué archivos no deben versionarse.
- `manage.py`: permite ejecutar comandos administrativos de Django.
- `README.md`: contiene la documentación del proyecto.

## Archivos que deben versionarse

Se deben incluir en Git:

- El código fuente del proyecto.
- Los archivos de migración de Django.
- `requirements.txt`.
- `.env.example`.
- `README.md`.
- Las plantillas y pruebas.

No se deben subir:

- `.env`.
- El entorno virtual `.venv/`.
- Contraseñas o credenciales privadas.
- Copias de seguridad con datos reales de la base de datos.
- Archivos temporales o caché de Python.
