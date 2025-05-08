from fastapi import FastAPI
from src.routes import healthy_route, product_route

app = FastAPI()

app.include_router(healthy_route.router, prefix="/healthy")
app.include_router(product_route.router, prefix="/product")
