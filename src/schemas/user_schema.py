from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    id: None = None
    name: str
    lastname: str
    email: EmailStr
    country: str 
    city: str
    password: str
    role: str

class UserUpdate(BaseModel):
    name: str | None = None
    lastname: str | None = None
    email: EmailStr | None = None
    country: str | None = None
    city: str | None = None
    password: str | None = None
    role: str | None = None