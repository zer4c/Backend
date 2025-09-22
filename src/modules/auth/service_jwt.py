import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from fastapi import HTTPException, Request
from jwt import ExpiredSignatureError, PyJWTError, decode, encode

from src.database import SessionDep
from src.modules.users import service

load_dotenv()
CRYPT_KEY = os.getenv("CRYPT_KEY")
TIME_EXPIRATION = os.getenv("TIME_EXPIRATION")
TIME_EXPIRATION = int(TIME_EXPIRATION)


def generate_access_token(sub: int):
    if not CRYPT_KEY:
        raise TypeError("Crypt key not found")
    if not TIME_EXPIRATION:
        raise TypeError("Time expiration not found")
    time_loc = datetime.now()
    expiration = time_loc + timedelta(hours=TIME_EXPIRATION)

    payload = {"sub": str(sub), "exp": expiration, "iat": time_loc}
    token = encode(payload, key=CRYPT_KEY, algorithm="HS256")
    return token


def validate_session_user(request: Request, session: SessionDep):
    try:
        if "authorization" not in request.headers:
            raise HTTPException(status_code=401, detail="Unauthorized")
        auth = request.headers["authorization"]

        if not auth.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Unauthorized")

        token_string = auth.removeprefix("Bearer ")

        payload = decode(token_string, key=CRYPT_KEY, algorithms=["HS256"])

        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token payload")

        user = service.get_user(int(user_id), session)
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return user

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")

    except PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    except Exception:
        raise HTTPException(status_code=401, detail="Unauthorized")


def validate_role(request: Request, session: SessionDep):
    auth = request.headers["authorization"]
    text_bearer = auth.removeprefix("Bearer ")
    token = decode(text_bearer, key=CRYPT_KEY, algorithms=["HS256"])
    user = service.get_user(token["sub"], session)
    if not user:
        raise HTTPException(status_code=403, detail="Forbidden")
    if user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Forbidden")
