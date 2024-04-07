### Hi there 👋

```python
print("I'm Emiliano Brizuela")

```

### Fullstack Developer from Argentina 🇦🇷

### Proyects

<img align="center" width="100%" src="https://firebasestorage.googleapis.com/v0/b/imagenes-memo.appspot.com/o/Captura%20de%20pantalla%202024-04-07%20a%20la(s)%201.33.56%E2%80%AFp.%C2%A0m..png?alt=media&token=e7742a1b-db86-47ed-b5a8-f0c4f8b0ff47">


# StockControl

StockControl es una aplicación para el control de inventario y gestión de proveedores.

## Instalación

1. Clona el repositorio desde GitHub:

    ```bash
    git clone https://github.com/emybr/trabajoFinalPython.git
    ```

2. Instala los requerimientos del proyecto utilizando pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Realiza las migraciones necesarias para configurar la base de datos:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

5. Accede a la aplicación desde tu navegador web ingresando la siguiente URL:

    ```
    http://localhost:8000/
    ```

## Funcionalidades

La aplicación StockControl proporciona las siguientes funcionalidades:

### Proveedores

- Agregar un nuevo proveedor con los siguientes detalles:
  - Nombre (texto)
  - Apellido (texto)
  - DNI (entero)

### Productos

- Agregar un nuevo producto con los siguientes detalles:
  - Nombre (texto)
  - Precio (flotante o entero)
  - Stock actual (entero)
  - Proveedor (relación ForeignKey con el modelo Proveedor)
