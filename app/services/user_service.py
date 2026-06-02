class UserService:
  def __init__(self, repo):
    self.repo = repo

  async def create_user(self, data):
    return await self.repo.create_user(data)
  
  async def get_users(self):
    return await self.repo.get_users()