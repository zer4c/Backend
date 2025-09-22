import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv
from fastapi import HTTPException

from src.modules.auth.schema import LoginInf
from src.modules.users import service as user_service
from src.database import SessionDep
from src.modules.auth import service_jwt

load_dotenv()

CRYPT_KEY = os.getenv("CRYPT_KEY")
fernet = Fernet(CRYPT_KEY)


def login_user(data: LoginInf, session: SessionDep):
    user = user_service.get_user_by_email(session, data.email)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid user")

    user.password = fernet.decrypt(user.password.encode()).decode()
    if user.password != data.password:
        raise HTTPException(status_code=401, detail="Incorrect Password")
    token = service_jwt.generate_access_token(user.id)
    return token
