from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.routes.user_routes import router as user_router
from app.database.session import engine
from app.database.base import Base

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

@app.get("/health")
def health_check():
  return {"status": "ok"}