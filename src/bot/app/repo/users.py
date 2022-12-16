from app.db.base_repository import BaseRepository
from app.models import User


class UserRepository(BaseRepository[User]):
    pass


user = UserRepository(User)
