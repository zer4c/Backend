from fastapi import APIRouter

from src.modules.health.controller import healthy_response

router = APIRouter()


@router.get("/")
def check_on():
    return healthy_response()
