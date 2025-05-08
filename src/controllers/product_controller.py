import src.services.product_service as ps 
from typing import Optional

def add_product_response(product: dict) -> str:
    if product['id'] is None:
        ps.add_product(product)
        return "Se añadio el producto"
    else: 
        print(list(product.keys()))
        return "error 400 Bad request"

def get_products_response():
    return ps.get_all_products()

def get_products_id_response(id: int) -> Optional[dict]:
    data = ps.get_product_by_id(id)
    if data is None:
        return data
    else:
        return "error 404 not Found"
    
def remove_product_response(id: int) -> Optional[str]:
    data = ps.remove_product(id)
    if data is None:
        return "error 404 not Found"

def update_product_response(product: dict) -> Optional[str]:
    if id not in product:
        return "error 400 Bad request"
    else:
        ps.update_product(product)

def patch_product_response(info: dict) -> Optional[str]:
    if id not in info:
        return "error 404 Bad request"
    else:
        ps.patch_product(info)
