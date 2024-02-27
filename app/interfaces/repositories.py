from abc import ABC, abstractmethod
from app.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        pass
