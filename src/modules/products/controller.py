import src.modules.products.service as ps
from src.modules.products.schema import Product


def add_product_response(product: Product) -> str:
    product = product.model_dump()
    if product["id"] is None:
        ps.add_product(product)
        return "Se añadio el producto"
    else:
        return "error 400 Bad request"


def get_products_response(
    brand: str | None,
    stockover: str | None,
    stockbelow: str | None,
    discountover: str | None,
    discountbelow: str | None,
    expireover: str | None,
    expirebelow: str | None,
) -> list | str:
    response = []
    if not any(
        [
            brand,
            stockbelow,
            stockover,
            discountbelow,
            discountover,
            expireover,
            expirebelow,
        ]
    ):
        return ps.get_all_products()
    elif brand:
        response = ps.filter_get_by_brand(brand.lower())
    elif stockover:
        stockover = int(stockover)
        response = ps.filter_get_by_stockover(stockover)
    elif stockbelow:
        stockbelow = int(stockbelow)
        response = ps.filter_get_by_stockbelow(stockbelow)
    elif discountover:
        discountover = int(discountover)
        response = ps.filter_get_by_discountover(discountover)
    elif discountbelow:
        discountbelow = int(discountbelow)
        response = ps.filter_get_by_discountbelow(discountbelow)
    elif expireover:
        response = ps.filter_get_by_expireover(int(expireover.replace("-", "")))
    elif expirebelow:
        response = ps.filter_get_by_expirebelow(int(expirebelow.replace("-", "")))
    else:
        response = "error 400 Bad Request"
    if type(response) is list and len(response) == 0:
        response = "error 404 Ningun producto encontrado"
    return response


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
