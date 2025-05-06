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



