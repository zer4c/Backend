from fastapi import APIRouter

import src.modules.products.controller as pc
from src.modules.products.schema import Product

router = APIRouter()


@router.post("/")
def add_product(product: Product):
    return pc.add_product_response(product)


@router.get("/")
def all_products(
    brand: str | None = None,
    stockover: str | None = None,
    stockbelow: str | None = None,
    discountover: str | None = None,
    discountbelow: str | None = None,
    expireover: str | None = None,
    expirebelow: str | None = None,
):
    return pc.get_products_response(
        brand,
        stockover,
        stockbelow,
        discountover,
        discountbelow,
        expireover,
        expirebelow,
    )


@router.get("/:{id}")
def get_product_id(id):
    return pc.get_products_id_response(id)


@router.put("/:{id}")
def update_product(product: Product, id):
    return pc.update_product_response(product, id)


@router.patch("/:{id}")
def patch_product(product: Product, id):
    return pc.patch_product_response(product, id)


@router.delete("/:{id}")
def remove_product(id):
    return pc.remove_product_response(id)
