from fastapi import APIRouter, status

from src.database import SessionDep
from src.modules.auth import controller
from src.modules.auth.schema import LoginInf
from src.modules.users.schema import UserCreate
from src.modules.users.model import User

router = APIRouter()


@router.post("/login", status_code=status.HTTP_200_OK)
def login_user(login_info: LoginInf, session: SessionDep):
    return controller.login_response(login_info, session)


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, session: SessionDep):
    return controller.register_user(User(**user.model_dump()), session)


# @router.delete('logout', status_code=status.HTTP_204_NO_CONTENT)
