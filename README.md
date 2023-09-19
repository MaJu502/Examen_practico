# Prototipo de Control de Empleados

Este Prototipo es un sistema web diseñado para el control de empleados en una empresa. Permite gestionar la información de empleados y departamentos, incluyendo la creación, actualización y eliminación de registros.

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

1. Clone este repositorio en su máquina:

    ```bash
    git clone https://github.com/tuusuario/proyecto-control-empleados.git
    cd proyecto-control-empleados
    ```

    a. Cree un entorno virtual (recomendado) para el proyecto:

            ```bash
            python -m venv venv
            ```
    b. Active el entorno virtual (en Windows):

            ```bash
            venv\Scripts\activate
            ```
    O, en macOS/Linux:

            ```bash
            source venv/bin/activate
            ```
    c. Instale las dependencias del proyecto, incluyendo Flask y psycopg2:

            ```bash
            pip install flask
            pip install psycopg2
            ```
    d. Configure la base de datos PostgreSQL con sus credenciales y detalles de conexión en el archivo backend/backendModel.py.

    e. Ejecute la aplicación Flask:

            ```bash
           python app.py
            ``
    f. Abra su navegador y vaya a http://localhost:5000 para acceder a la aplicación.