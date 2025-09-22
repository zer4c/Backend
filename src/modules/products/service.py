import json
from typing import Optional


def __load_data():
    with open("src/assets/data.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)


data_cache = __load_data()


def add_product(product: dict) -> None:
    maxi = 0
    for products in data_cache:
        if maxi < int(products["id"]):
            maxi = int(products["id"])
    product["id"] = str(maxi + 1)
    data_cache.append(product)


def get_all_products() -> list:
    return data_cache


def get_product_by_id(id: int) -> Optional[dict]:
    data = data_cache
    produc = next((prod for prod in data if prod["id"] == id), None)
    return produc


def remove_product(id: int) -> Optional[dict]:
    for i, prod in enumerate(data_cache):
        if prod.get("id") == id:
            return data_cache.pop(i)
    return None


def update_product(product: dict, id: int) -> None | dict:
    produc_act = get_product_by_id(id)
    if produc_act is not None:
        remove_product(id)
        data_cache.append(product)
        return product
    else:
        return None


def patch_product(info: dict, id: int) -> None | dict:
    product = get_product_by_id(id)
    if product is not None:
        for key in list(info.keys()):
            if info[key] is not None:
                product[key] = info[key]
        return info
    else:
        return None


def filter_get_by_brand(brand: str) -> list:
    data = []
    for product in data_cache:
        if product["brand"].lower() == brand:
            data.append(product)
    return data


def filter_get_by_stockover(stockover: int) -> list:
    data = []
    for product in data_cache:
        if int(product["stock"]) >= stockover:
            data.append(product)
    return data


def filter_get_by_stockbelow(stockbelow: int) -> list:
    data = []
    for product in data_cache:
        if int(product["stock"]) < stockbelow:
            data.append(product)
    return data


def filter_get_by_discountbelow(discountbelow: int) -> list:
    data = []
    for product in data_cache:
        if int(product["discount"]) < discountbelow:
            data.append(product)
    return data


def filter_get_by_discountover(discountover: int) -> list:
    data = []
    for product in data_cache:
        if int(product["discount"]) >= discountover:
            data.append(product)
    return data


def filter_get_by_expireover(expireover: int) -> list:
    data = []
    for product in data_cache:
        if int(product["expiration"].replace("-", "")) >= expireover:
            data.append(product)
    return data


def filter_get_by_expirebelow(expirebelow: int) -> list:
    data = []
    for product in data_cache:
        if int(product["expiration"].replace("-", "")) < expirebelow:
            data.append(product)
    return data
