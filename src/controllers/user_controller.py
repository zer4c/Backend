import src.services.user_service as us
from fastapi import exceptions
from src.models.user_model import User

def add_user_response(user: User, session):
    if user.id is not None:
        raise exceptions.HTTPException(
            status_code=400,
            detail="User ID must be None for new users."
        )
    if not all([
        user.name,
        user.lastname,
        user.email,
        user.country,
        user.city,
        user.password,
    ]):
        raise exceptions.HTTPException(
            status_code=400,
            detail="User data is incomplete."
        )
    us.add_user(user, session)
    return "user added successfully"

def get_all_users_response(session, city, country, email):
    users = us.get_all_users(session, city, country, email)
    if not users:
        raise exceptions.HTTPException(
            status_code=404,
            detail="No users found"
        )
    return users

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
    return user

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
    return "User deleted successfully"

def update_user_response(user: User, id: int, session):
    if not id:
        raise exceptions.HTTPException(
            status_code=400,
            detail="User ID must not be None."
        )
    if not all([
        user.name,
        user.lastname,
        user.email,
        user.country,
        user.city,
        user.password,
    ]): 
        raise exceptions.HTTPException(
            status_code=400,
            detail="User data is incomplete."
        )
    user = us.update_user(user, id, session)
    if not user:
        raise exceptions.HTTPException(
            status_code=404,
            detail="User not found"
        )
    return "User updated successfully"

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
    return "User patched successfully"