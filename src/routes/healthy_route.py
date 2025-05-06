from fastapi import APIRouter
from src.controllers.healthy_controller import healthy_response

router = APIRouter()

@router.get("/")
def check_on():
    return healthy_response()
