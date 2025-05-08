from pydantic import BaseModel

class Product(BaseModel):
    id: str | None = None
    name: str
    brand: str | None = None
    stock: int
    batch: str
    expiration: str
    discount: float | None = None
