from fastapi import APIRouter, status
from src.models.user import User
from src.database import SessionDep

import src.controllers.user_controller as uc

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_user(user: User, session: SessionDep):
    return uc.add_user_response(user, session)

@router.get("/", status_code=status.HTTP_200_OK)
def get_all_users(session: SessionDep):
    return uc.get_all_users_response(session)