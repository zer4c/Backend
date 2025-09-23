import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv
from fastapi import HTTPException

from src.modules.auth.schema import LoginInf, LogoutInf
from src.modules.users import service as user_service
from src.modules.database.database import SessionDep
from src.modules.auth import service_jwt
from src.modules.database.redis import get_redis_session

load_dotenv()

CRYPT_KEY = os.getenv("CRYPT_KEY")
fernet = Fernet(CRYPT_KEY)


def login_user(data: LoginInf, session: SessionDep):
    redis = get_redis_session()
    user_cache = redis.get(data.email)
    if user_cache:
        raise HTTPException(status_code=400, detail="User already loggin in")
    user = user_service.get_user_by_email(session, data.email)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid user")

    user.password = fernet.decrypt(user.password.encode()).decode()
    if user.password != data.password:
        raise HTTPException(status_code=401, detail="Incorrect Password")
    token = service_jwt.generate_access_token(user.id, user.email)
    redis.close()
    return token


def logout_user(data: LogoutInf):
    redis = get_redis_session()
    user = redis.get(data.email)
    if not user:
        raise HTTPException(status_code=400, detail="Bad Request")
    redis.delete(data.email)
    redis.close()
