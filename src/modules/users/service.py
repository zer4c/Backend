import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv
from fastapi import HTTPException
from sqlmodel import select

from src.database import SessionDep
from src.modules.users.model import User

load_dotenv()

CRYPT_KEY = os.getenv("CRYPT_KEY")
fernet = Fernet(CRYPT_KEY)


def add_user(user: User, session: SessionDep):
    user.password = fernet.encrypt(user.password.encode()).decode()
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()


def get_all_users(session, city, country, email):
    if city and country:
        users = session.exec(
            select(User).where(User.city == city, User.country == country)
        ).all()
    elif email:
        users = session.exec(select(User).where(User.email == email)).all()
    elif city:
        users = session.exec(select(User).where(User.city == city)).all()
    elif country:
        users = session.exec(select(User).where(User.country == country)).all()
    else:
        users = session.exec(select(User)).all()
    session.close()
    return users


def get_user_by_email(session: SessionDep, email: str):
    user = session.exec(select(User).where(User.email == email)).all()
    session.close()
    return user


def get_user(id: int, session: SessionDep):
    user = session.get(User, id)
    if not user:
        session.close()
        return None
    session.close()
    return user


def remove_user(id: int, session: SessionDep):
    user = session.get(User, id)
    if not user:
        session.close()
        return None
    session.delete(user)
    session.commit()
    session.close()
    return user


def update_user(user: User, id: int, session: SessionDep):
    user_search = session.get(User, id)
    if not user_search:
        session.close()
        return None

    for key in user.model_dump(exclude_unset=True).keys():
        if key != "password":
            setattr(user_search, key, getattr(user, key))
    user_search.password = fernet.encrypt(user.password.encode()).decode()

    session.add(user_search)
    session.commit()
    session.refresh(user_search)
    session.close()
    return user_search


def patch_user(user: User, id: int, session: SessionDep):
    user_search = session.get(User, id)
    if not user_search:
        session.close()
        return None
    user_dump = user.model_dump(exclude_unset=True)
    old_email = user_search.email
    for key in user_dump.keys():
        if not user_dump[key]:
            continue
        if key == "password":
            if "email" not in user_dump.keys() or user_dump["email"] != old_email:
                raise HTTPException(
                    status_code=400, detail="Password cannot be updated."
                )
            user_search.password = fernet.encrypt(user_dump[key].encode()).decode()
        else:
            setattr(user_search, key, user_dump[key])

    session.add(user_search)
    session.commit()
    session.refresh(user_search)
    session.close()
    return user_search
