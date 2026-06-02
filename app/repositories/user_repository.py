from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user_model import User

class UserRepository:
  def __init__(self, session: AsyncSession):
    self.session = session

  async def create_user(self, name: str, email: str):
    user = User(name=name, email=email)

    self.session.add(user)
    await self.session.commit()
    await self.session.refresh(user)

    return user
  
  async def get_users(self):
    result = await self.session.execute(select(User))
    return result.scalar().all()
  
  async def get_user_by_id(self, user_id: int):
    result = await self.session.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()