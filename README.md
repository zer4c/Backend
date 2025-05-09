## Dependencias

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- conda o [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install)

## Intalacion

```
git clone git@github.com:zer4c/Backend.git
cd backend    
conda env create -f enviroment.yml
conda activate backend
uv sync
```
## Uso de proyecto

`fastapi dev main.py`

Esto iniciara el servicio en localhost:8000

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

    