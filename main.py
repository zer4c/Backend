from fastapi import FastAPI
from src.routes import healthy_route, product_route, user_route
from src.database import iniciate_database
from contextlib import asynccontextmanager

@asynccontextmanager
async def iniciate_app(app: FastAPI):
    iniciate_database()
    yield
    print("terminate")

app = FastAPI(lifespan=iniciate_app)

app.include_router(healthy_route.router, prefix="/healthy")
app.include_router(product_route.router, prefix="/product")
app.include_router(user_route.router, prefix="/user")