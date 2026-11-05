# ClassroomHub

## Descripción del proyecto

ClassroomHub es una aplicación web desarrollada con Django como parte de un ejercicio de aprendizaje. Su objetivo es ofrecer un sitio web sencillo donde los usuarios puedan consultar recursos educativos y conocer información sobre el proyecto.

## Funcionalidades

- **Página de inicio:** muestra un mensaje de bienvenida.
- **Página de recursos:** presenta diferentes recursos educativos.
- **Página Acerca de:** contiene información sobre el propósito del proyecto.
- **Página FAQ:** presenta preguntas frecuentes y sus respectivas respuestas.
- **Menú de navegación:** permite desplazarse entre las diferentes secciones del sitio web.

## Tecnologías utilizadas

- Python
- Django
- HTML
- Git
- GitHub

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/ra-cmyk16/laboratorio-6-.git
   ```

2. Ingresar a la carpeta del proyecto:

   ```bash
   cd laboratorio-6-
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución del proyecto

Para iniciar el servidor de desarrollo, ejecutar:

```bash
python manage.py runserver
```

Después, abrir el navegador y visitar la siguiente dirección:

http://127.0.0.1:8000/

## Ejecución de pruebas

Para ejecutar las pruebas automatizadas de la aplicación, utilizar:

```bash
python manage.py test pages
```

## Estructura del proyecto

- `config/`: contiene la configuración principal del proyecto Django.
- `pages/`: contiene las vistas, rutas, pruebas y plantillas de las páginas.
- `requirements.txt`: contiene las dependencias necesarias para ejecutar el proyecto.
- `manage.py`: permite ejecutar comandos administrativos de Django.
- `README.md`: contiene la documentación general del proyecto.

## Autor

Proyecto desarrollado como parte de un ejercicio académico de aprendizaje de Django.