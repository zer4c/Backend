import src.services.user_service as us
from fastapi import exceptions
from src.models.user_model import User
from src.schemas.response_schema import IResponse
from src.schemas.user_dto import UserDTO

def __convert_DTO(user: User):
    user_dto = UserDTO(
        name=user.name,
        lastname=user.lastname,
        email=user.email,
        country=user.country,
        city=user.city,
        role=user.role
    )
    return user_dto

def add_user_response(user: User, session):
    us.add_user(user, session)
    
    user_dto = __convert_DTO(user)

    response = IResponse(
        detail="User added Succesfully",
        status_code=201,
        ok=True,
        data=user_dto
    )
    return response

def get_all_users_response(session, city, country, email):
    users = us.get_all_users(session, city, country, email)
    if not users:
        raise exceptions.HTTPException(
            status_code=404,
            detail="No users found"
        )
    users_dto = [__convert_DTO(user) for user in users]

    response = IResponse(
        detail="users found",
        status_code=200,
        data=users_dto
    )
    return response

def get_user_response(id: int, session):
    if id is None:
        raise exceptions.HTTPException(
            status_code=400,
            detail="User ID must not be None."
        )
    user = us.get_user(id, session)
    if not user:
        raise exceptions.HTTPException(
            status_code=404,
            detail="User not found"
        )
    user_dto = __convert_DTO(user)

    response = IResponse(
        detail="user founded succesfully",
        status_code=200,
        data = user_dto
    )

    return response

def delete_user_response(id: int, session):
    if id is None:
        raise exceptions.HTTPException(
            status_code=400,
            detail="User ID must not be None."
        )
    user = us.remove_user(id, session)
    if not user:
        raise exceptions.HTTPException(
            status_code=404,
            detail="User not found"
        )
    response = IResponse(
        detail="User deleted successfully",
        status_code=204,
    )
    return response

def update_user_response(user: User, id: int, session):
    if not id:
        raise exceptions.HTTPException(
            status_code=400,
            detail="User ID must not be None."
        )
    user = us.update_user(user, id, session)
    if not user:
        raise exceptions.HTTPException(
            status_code=404,
            detail="User not found"
        )
    user_dto = __convert_DTO(user)
    response = IResponse(
        detail="user updated succesfully",
        status_code=200,
        data=user_dto
    )
    return response

def patch_user_response(user: User, id: int, session):
    if not id:
        raise exceptions.HTTPException(
            status_code=400,
            detail="User ID must not be None."
        )
    if not any([
        user.name,
        user.lastname,
        user.email,
        user.country,
        user.city,
        user.password,
    ]):
        raise exceptions.HTTPException(
            status_code=400,
            detail="No fields to update."
        )
    patch_user = us.patch_user(user, id, session)
    if not patch_user:
        raise exceptions.HTTPException(
            status_code=404,
            detail="User not found"
        )
    user_dto = __convert_DTO(patch_user)

    response = IResponse(
        detail="User patched successfully",
        status_code=200,
        data=user_dto
    )
    return response