from app.entities.user import User
from app.interfaces.repositories import UserRepository


class UserRegistration:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, username: str, email: str, password: str) -> User:
        user = User(username, email, password)
        return self.user_repository.save(user)
