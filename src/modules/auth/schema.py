from pydantic import BaseModel, EmailStr


class LoginInf(BaseModel):
    email: EmailStr
    password: str

class LogoutInf(BaseModel):
    email: EmailStr
    token: str