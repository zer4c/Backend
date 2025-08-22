from fastapi import HTTPException, Request
from jwt import decode
from dotenv import load_dotenv
from src.database import SessionDep
from src.services.user_service import get_user
import os

load_dotenv()
CRYPT_KEY = os.getenv("CRYPT_KEY")

def validate_user(request: Request, session: SessionDep):
    if "authorization" not in request.headers:
        raise HTTPException(status_code=401, 
                            detail="authorization header missing")
    auth = request.headers["authorization"]
    if not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, 
                            detail="authorization must be bearer")
    
    text_bearer = auth.removeprefix("Bearer ")
    
    token = decode(text_bearer,key=CRYPT_KEY, algorithms=["HS256"])
    user = get_user(token['id'], session)
    if not user:
        raise HTTPException(status_code=404,
                            detail='User not found')
    if user.role != 'ADMIN':
        raise HTTPException(status_code=401,
                            detail='you need is a Admin'

        )
    
