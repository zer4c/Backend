import json 
from typing import Optional

def __load_data():
    with open("src/assets/data.json", 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

data_cache = __load_data()

def add_product(product: dict) -> None:
    maxi = 0
    for products in data_cache:
        if(maxi < int(products['id'])):
            maxi = int(products['id'])
    product['id'] = str(maxi+1)
    data_cache.append(product)

def get_all_products() -> list:
    return data_cache

def get_product_by_id(id: int) -> Optional[dict]:
    data = data_cache
    produc = next((prod for prod in data if prod['id'] == id), None)
    return produc

def remove_product(id: int)-> Optional[dict]:
    for i, prod in enumerate(data_cache):
        if prod.get('id') == id:
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
        print(list(info.keys()))
        print(list(product.keys()))
        for key in list(info.keys()):
            if info[key] is not None:
                product[key] = info[key] 
        return info
    else:
        return None



