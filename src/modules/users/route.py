from fastapi import APIRouter, Depends, status

import src.modules.users.controller as uc
from src.modules.auth.service_jwt import validate_role
from src.database import SessionDep
from src.modules.users.model import User
from src.modules.users.schema import UserCreate, UserPatch, UserUpdate

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_user(
    user: UserCreate, session: SessionDep, validate_role: str = Depends(validate_role)
):
    return uc.add_user_response(User(**user.model_dump()), session)


@router.get("/", status_code=status.HTTP_200_OK)
def get_all_users(
    session: SessionDep,
    city: str | None = None,
    country: str | None = None,
    email: str | None = None,
):
    return uc.get_all_users_response(session, city, country, email)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_user(id: int, session: SessionDep):
    return uc.get_user_response(id, session)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    id: int, session: SessionDep, validate_role: str = Depends(validate_role)
):
    return uc.delete_user_response(id, session)


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_user(
    user: UserUpdate,
    id: int,
    session: SessionDep,
    validate_role: str = Depends(validate_role),
):
    return uc.update_user_response(User(**user.model_dump()), id, session)


@router.patch("/{id}", status_code=status.HTTP_200_OK)
def patch_user(
    user: UserPatch,
    id: int,
    session: SessionDep,
    validate_role: str = Depends(validate_role),
):
    return uc.patch_user_response(User(**user.model_dump()), id, session)
