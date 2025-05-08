import json 
from typing import Optional

def __load_data():
    with open("../assets/data.json", 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

data_cache = __load_data()

def add_product(product: dict) -> None:
    maxi = 0
    for products in data_cache:
        if(maxi < products['id']):
            maxi = products['id']
    product['id'] = maxi+1
    data_cache.append(product)

def get_all_products() -> list:
    return data_cache

def get_product_by_id(id: int) -> Optional[dict]:
    data = data_cache
    produc = next((prod for prod in data if prod['id'] == id), None)
    return produc

def remove_product(id: int) -> None:
    i = 0
    for prod in data_cache:
        if(prod['id'] != id):
            i = i + 1
        else: 
            break
    data_cache.pop(i)

def update_product(product: dict) -> None:
    id = product['id']
    produc_act = get_product_by_id(id)
    if(produc_act != None):
        remove_product(id)
        data_cache.append(product)

def patch_product(info: dict) -> None:
    id = info['id']
    product = get_product_by_id(id)
    if(product != None):
        keys = list(info.keys())
        for key in keys:
            product[key] = info[key] 



