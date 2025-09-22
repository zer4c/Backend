import os

from dotenv import load_dotenv
from fastapi import HTTPException, Request
from jwt import decode
from datetime import datetime, timedelta

from src.database import SessionDep
from src.modules.users import service

load_dotenv()
CRYPT_KEY = os.getenv("CRYPT_KEY")
TIME_EXPIRATION = os.getenv("TIME_EXPIRATION")


def generate_access_token(sub: int):
    if not CRYPT_KEY:
        raise TypeError("Crypt key not found")
    if not TIME_EXPIRATION:
        raise TypeError("Time expiration not found")
    time_loc = datetime.now()
    expiration = time_loc + timedelta(hours=TIME_EXPIRATION)

    payload = {"sub": sub, "exp": str(expiration), "iat": str(time_loc)}
    return payload


def validate_session_user(request: Request, session: SessionDep):
    if "authorization" not in request.headers:
        raise HTTPException(status_code=401, detail="Unauthorized")
    auth = request.headers["authorization"]

    if not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")

    text_bearer = auth.removeprefix("Bearer ")

    token = decode(text_bearer, key=CRYPT_KEY, algorithms=["HS256"])
    user = service.get_user(token["sub"], session)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    request.user = user


def validate_role(request: Request):
    user = request.user
    if not user:
        raise HTTPException(status_code=403, detail="Forbidden")
    if user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Forbidden")
