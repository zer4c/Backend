from fastapi import HTTPException

from src.config.response_schema import IResponse
from src.database import SessionDep
from src.modules.auth import service
from src.modules.auth.schema import LoginInf
from src.modules.users import service as user_service
from src.modules.users.model import User
from src.modules.users.schema_dto import UserDTO


def login_response(data: LoginInf, session: SessionDep):
    user = service.login_user(data, session)
    return user


def register_user(user: User, session: SessionDep):
    user_search = user_service.get_user_by_email(session, user.email)
    if user_search:
        raise HTTPException(status_code=400, detail="Email already used")
    user_service.add_user(user, session)

    user_dto = UserDTO(
        name=user.name,
        lastname=user.lastname,
        email=user.email,
        country=user.country,
        city=user.city,
        role=user.role,
    )

    response = IResponse(
        detail="User added Succesfully", status_code=201, ok=True, data=user_dto
    )
    return response
