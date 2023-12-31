# Prototipo de Control de Empleados

Este Prototipo es un sistema web diseñado para el control de empleados en una empresa bajo el patron MVC. Permite gestionar la información de empleados y departamentos, incluyendo la creación, actualización y eliminación de registros.

## Características

- Listar todos los empleados y departamentos en una tabla.
- Crear un nuevo empleado o departamento.
- Actualizar un empleado o departamento existente.
- Eliminar un empleado o departamento.
- Verificar la existencia de empleados y departamentos antes de realizar acciones de actualización o eliminación.

## Tecnologías Utilizadas

- Python
- Flask (framework web)
- PostgreSQL (base de datos)
- HTML y CSS (para la interfaz de usuario)

## Instalación

Siga estos pasos para configurar y ejecutar el proyecto en su entorno local:

1. **Clone este repositorio en su máquina:**

    ```bash
    git clone https://github.com/tuusuario/proyecto-control-empleados.git
    cd proyecto-control-empleados
    ```

2. **Cree un entorno virtual (recomendado) para el proyecto:**

    ```bash
    python -m venv venv
    ```

3. **Active el entorno virtual (en Windows):**

    ```bash
    venv\Scripts\activate
    ```

    O, en macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

4. **Instale las dependencias del proyecto, incluyendo Flask y psycopg2:**

    ```bash
    pip install flask
    pip install psycopg2
    ```

5. **Configure la base de datos PostgreSQL:**

   - Edite el archivo `backend/backendModel.py` y configure las credenciales y detalles de conexión.

6. **Ejecute la aplicación Flask:**

    ```bash
    python app.py
    ```

7. **Abra su navegador y vaya a http://localhost:5000 para acceder a la aplicación.**

## Uso
- Navegue por la aplicación para listar, crear, actualizar y eliminar empleados y departamentos.
- Utilice las funciones de verificación para asegurarse de que los registros existan antes de realizar acciones de actualización o eliminación.

## Contribuciones
Si desea contribuir a este proyecto, abra un problema o envíe una solicitud de extracción. Estamos abiertos a mejoras y nuevas características.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulte el archivo LICENSE para más detalles.

## Requisitos del Sistema

- Python 3.x
- PostgreSQL 12.x

## Estructura del Proyecto
El proyecto está organizado de la siguiente manera:

## Capturas de Pantalla
![Alt text](/static/test_images/image.png)

![Alt text](/static/test_images/image-1.png)

![Alt text](/static/test_images/image-2.png)