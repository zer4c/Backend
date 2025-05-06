from fastapi import FastAPI
from src.routes import healthy_route

app = FastAPI()

app.include_router(healthy_route.router, prefix="/healthy")
