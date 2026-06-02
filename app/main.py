from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.routes.user_routes import router as user_router
from app.database.session import engine
from app.database.base import Base
from app.core.errors import NotFoundError, ConflictError
from app.core.exception_handlers import app_exception_handler, not_found_handler, conflict_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)
  yield

app = FastAPI(
  title="User API",
  version="1.0.0", 
  lifespan=lifespan
)

app.include_router(user_router)

app.add_exception_handler(Exception, app_exception_handler)
app.add_exception_handler(NotFoundError, not_found_handler)
app.add_exception_handler(ConflictError, conflict_handler)

@app.get("/health")
def health_check():
  return {"status": "ok"}