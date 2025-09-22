from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    lastname: str
    email: str
    country: str
    city: str
    password: str
    role: str
