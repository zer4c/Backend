## Dependencias

- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Intalacion

```
git clone git@github.com:zer4c/Backend.git
cd backend    
uv sync
```
## Uso de proyecto

al hacer el el comando anterior `uv sync`, la herramienta uv creara un .venv local
para activar este entorno virtual utilice: 

`source .venv/bin/activate`

para desactivarlo utilice:

`deactivate`

mientras este activado el entorno virtual puede ejecutar el proyecto. 

`fastapi dev main.py`

Esto iniciara el servicio en localhost:8000 y se refrescara con cada cambio, pero esto
solo es para desarrollo.



## Servicios

- Healthy - localhost:8000/healthy/ 
- Product CRUD - localhost:800/product/
    - todos los productos `get /product/`
    - enviar producto `post /product/`
    - obtener un solo producto `get /product/:id`
    - eliminar un producto `delete /product/:id`
    - actualizar un producto `put /product/:id`
    - actualizar parte de producto `patch /product/:id`
- filtros de productos por medio de query params solo uno a la vez
    - por "brand"
    - por "stockover" y "stockbelow"
    - por "discountover" y "discountbelow"
    - por "expireover" y "expirebelow"

    