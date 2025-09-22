from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI

import src.modules.health.route as healthRoutes
import src.modules.products.route as productsRoutes
import src.modules.users.route as usersRoutes
from src.database import iniciate_database
from src.modules.auth.jwt import validate_session_user


@asynccontextmanager
async def iniciate_app(app: FastAPI):
    iniciate_database()
    yield
    print("terminate")


app = FastAPI(lifespan=iniciate_app)

app.include_router(healthRoutes.router, prefix="/healthy")
app.include_router(productsRoutes.router, prefix="/product")
app.include_router(
    usersRoutes.router, prefix="/user", dependencies=[Depends(validate_session_user)]
)
