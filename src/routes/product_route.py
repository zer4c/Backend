from fastapi import APIRouter
import src.controllers.product_controller as pc

router = APIRouter()

@router.post("/")
def add_product(product: dict):
    return pc.add_product_response()

@router.get("/")
def all_products():
    return pc.get_products_response()

@router.get("/{id}")
def get_product_id(id):
    return pc.get_products_id_response(id)

@router.put("/{id}")
def update_product(id):
    return pc.update_product_response(id)

@router.patch("/{id}")
def patch_product(id):
    return pc.patch_product_response(id)

@router.delete("/{id}")
def remove_product(id):
    return pc.remove_product_response(id)
