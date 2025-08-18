from fastapi import APIRouter, status
from src.models.user import User
from src.database import SessionDep

import src.controllers.user_controller as uc

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_user(user: User, session: SessionDep):
    return uc.add_user_response(user, session)

@router.get("/", status_code=status.HTTP_200_OK)
def get_all_users(session: SessionDep, 
                  city: str | None = None,
                  country: str | None = None,
                  email: str | None = None):
    return uc.get_all_users_response(session, city, country, email)

@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_user(id: int, session: SessionDep):
    return uc.get_user_response(id, session)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, session: SessionDep):
    return uc.delete_user_response(id, session)

@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_user(user: User, id: int, session: SessionDep):
    return uc.update_user_response(user, id, session)

@router.patch("/{id}", status_code=status.HTTP_200_OK)
def patch_user(user: User, id: int, session: SessionDep):
    return uc.patch_user_response(user, id, session)