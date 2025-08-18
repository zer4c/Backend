import src.services.user_service as us
from fastapi import exceptions
from src.models.user import User


def add_user_response(user: User, session):
    if user.id is not None:
        raise exceptions.HTTPException(
            status_code=400,
            detail="User ID must be None for new users."
        )
    us.add_user(user, session)
    return "user added successfully"

def get_all_users_response(session):
    users = us.get_all_users(session)
    if not users:
        raise exceptions.HTTPException(
            status_code=404,
            detail="No users found"
        )
    return users