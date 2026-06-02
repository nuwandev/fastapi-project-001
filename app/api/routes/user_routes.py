from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate, UserResponse
from app.schemas.response_schema import ApiResponse
from app.dependencies.user import get_user_repository, get_user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=ApiResponse[UserResponse])
async def create_user(
  user: UserCreate,
  service: UserService = Depends(get_user_service),
):
  user = await service.create_user(user)
  return ApiResponse(data=user)

@router.get("/{user_id}", response_model=ApiResponse[UserResponse])
async def get_user(
  user_id: int,
  service: UserService = Depends(get_user_service)
):
  user = await service.get_user_by_id(user_id)
  return ApiResponse(data=user)

@router.get("/", response_model=ApiResponse[list[UserResponse]])
async def get_users(
  service: UserService = Depends(get_user_service)
):
  users = await service.get_users()
  return ApiResponse(data=users)