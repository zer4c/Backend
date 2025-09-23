from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI

import src.modules.health.route as healthRoutes
import src.modules.products.route as productsRoutes
import src.modules.users.route as usersRoutes
import src.modules.auth.route as authRoutes
from src.modules.database.database import iniciate_database
from src.modules.auth.service_jwt import validate_session_user
from src.modules.database.redis import get_redis_session

@asynccontextmanager
async def iniciate_app(app: FastAPI):
    iniciate_database()
    redis_session = get_redis_session()
    yield
    redis_session.close()

app = FastAPI(lifespan=iniciate_app)

app.include_router(authRoutes.router, prefix="/auth")
app.include_router(healthRoutes.router, prefix="/healthy")
app.include_router(productsRoutes.router, prefix="/product")
app.include_router(
    usersRoutes.router, prefix="/user", dependencies=[Depends(validate_session_user)]
)
