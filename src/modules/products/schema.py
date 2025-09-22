from pydantic import BaseModel


class Product(BaseModel):
    id: str | None = None
    name: str | None = None
    brand: str | None = None
    stock: str | None = None
    batch: str | None = None
    expiration: str | None = None
    discount: float | None = None
