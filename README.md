# Descripcion

Este proyecto es una API REST hecha con el framework de Fastapi.

## Caracteristicas 

- Inicio de sesion y registro al sistema, donde las sesiones son tokens bearer.

- Ahora no se podra utilizar el endpoint users, si no estas logeado, validado por un midleware para toda el endpoint.

- Los usuarios tienen roles, ADMIN y USER, donde el administrador se valida mediante el sub proporcionado por el token bearer del login, este proceso se valida a travez de otro middleware.

- Utiliza Mysql como gestor de BBDD, en el codigo se maneja a travez del ORM sqlModel

- Autenticacion de datos a travez de modelos Pydantic.

- El proyecto utiliza el modelo Modelo-Vista-Controlador, y DTO para respuesta de los datos.

- se utilizo HTTPexceptions para los errores ocurridos en tiempo de ejecucion.

## Dependencias

- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Intalacion

```
git clone git@github.com:zer4c/Backend.git
cd backend    
uv sync
```
# Uso de proyecto

al hacer el el comando anterior `uv sync`, la herramienta uv creara un .venv local
para activar este entorno virtual utilice: 

`source .venv/bin/activate`

para desactivarlo utilice:

`deactivate`

Para levantar la BBDD tiene que utilizar:

`docker-compose up -d`

mientras este activado el entorno virtual puede ejecutar el proyecto. 

`fastapi dev main.py`

Esto iniciara el servicio en localhost:8000 y se refrescara con cada cambio, pero esto
solo es para desarrollo.

Al terminar todo utilice:

`docker-compose down`

## Servicios

### Healthy -
-  localhost:8000/healthy/ 
### Product CRUD 
- localhost:8000 product/
    - todos los productos `get /`
    - enviar producto `post  /`
    - obtener un solo producto `get  /:id`
    - eliminar un producto `delete  /:id`
    - actualizar un producto `put  /:id`
    - actualizar parte de producto `patch  /:id`
- filtros de productos por medio de query params solo uno a la vez
    - por "brand"
    - por "stockover" y "stockbelow"
    - por "discountover" y "discountbelow"
    - por "expireover" y "expirebelow"

### Users CRUD
los metodos post, patch, update y remove necesitan autenticacion con JWT bearer.

- localhost:8000/user/
    - añadir un usuario `post /`
    - Obtener todos los usuarios `get /`
    - Obtener el usuario con un id `get /:id`
    - Eliminar un usuario por un id `delete /:id`
    - Actualizar un usuario `put /:id`
    - Actualizar parte de un usuario `put /:id`
- filtros en get mediante query params, admite varios a la vez
    - city
    - country
    - email

### Auth

- localhost:8000/auth
    - loguear con una cuenta ya creada `post /login`
    - Registrar una nueva cuenta `post / register`