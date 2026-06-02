from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
async def create_user(
  user: UserCreate,
  db: AsyncSession = Depends(get_db)
):
  repo = UserRepository(db)
  service = UserService(repo)
  
  crated_user = await service.create_user(
    name=user.name,
    email=user.email
  )

  return crated_user

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
  user_id: int,
  db: AsyncSession = Depends(get_db)
):
  repo = UserRepository(db)
  service = UserService(repo)
  
  user = await service.get_user_by_id(user_id)

  return user

@router.get("/", response_model=list[UserResponse])
async def get_users(
  db: AsyncSession = Depends(get_db)
):
  repo = UserRepository(db)
  service = UserService(repo)
  
  users = await service.get_users()

  return users