from app.models.user_model import User

class UserRepository:

  def __init__(self, session):
    self.session = session

  async def create_user(self, user: User):
    self.session.add(user)
    await self.session.commit()
    await self.session.refresh(user)
    return user
  
  async def get_users(self):
    result = await self.session.execute(
      "SELECT * FROM users"
    )
    return result.fetchall()
