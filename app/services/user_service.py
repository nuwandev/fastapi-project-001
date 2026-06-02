from app.repositories.user_repository import UserRepository
class UserService:
  def __init__(self, repo: UserRepository):
    self.repo = repo

  async def create_user(self, name: str, email: str):
    return await self.repo.create_user(name, email)
  
  async def get_users(self):
    return await self.repo.get_users()
  
  async def get_user_by_id(self, user_id: int):
    return await self.repo.get_user_by_id(user_id)