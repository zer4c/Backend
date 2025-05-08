import src.services.product_service as ps 
from src.models.product import Product

def add_product_response(product: Product) -> str:
    product = product.model_dump()
    if product['id'] is None:
        ps.add_product(product)
        return "Se añadio el producto"
    else: 
        return "error 400 Bad request"

def get_products_response():
    return ps.get_all_products()

def get_products_id_response(id: int) -> Product | str:
    data = ps.get_product_by_id(id)
    if data is not None:
        return data
    else:
        return "error 404 not Found"
    
def remove_product_response(id: int) -> str:
    data = ps.remove_product(id)
    if data is None:
        return "error 404 not Found"
    else:
        return "Producto eliminado"

def update_product_response(product: Product, id: int) -> str:
    data = ps.update_product(product.model_dump(), id)
    if data is None:
        return "error 400 Bad request"
    else:
        return "producto Actualizado"

def patch_product_response(info: Product, id: int) -> str:
    data = ps.patch_product(info.model_dump(), id)
    if data is None:
        return "error 404 Bad request"
    else:
        return "Actualizacion parcial de producto"
