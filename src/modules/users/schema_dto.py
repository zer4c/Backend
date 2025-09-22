from pydantic import BaseModel


class UserDTO(BaseModel):
    name: str
    lastname: str
    email: str
    country: str
    city: str
    role: str
