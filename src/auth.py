from fastapi import HTTPException, Request
from jwt import decode
from dotenv import load_dotenv
import os

CRYPT_KEY = os.getenv("CRYPT_KEY")


def validate_user(request: Request):
    if "authorization" not in request.headers:
        raise HTTPException(status_code=401, 
                            detail="authorization header missing")
    auth = request.headers["authorization"]
    if not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, 
                            detail="authorization must be bearer")
    
    text_bearer = auth.removeprefix("Bearer ")
    
    token = decode(text_bearer,key=CRYPT_KEY, algorithms=["HS256"])
    if "ADMIN" not in token["role"]:
        raise HTTPException(status_code=403, 
                            detail="you need admin role")
    
