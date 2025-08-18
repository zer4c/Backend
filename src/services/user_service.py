from src.models.user import User
from sqlmodel import select

def add_user(user: User, session):
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()

def get_all_users(session):
    users = session.exec(select(User)).all()
    session.close()
    return users