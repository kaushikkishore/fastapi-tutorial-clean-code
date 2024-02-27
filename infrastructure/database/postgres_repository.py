from app.entities.user import User
from app.interfaces.repositories import UserRepository
import psycopg2


class PostgresUserRepository(UserRepository):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def save(self, user: User) -> User:
        conn = psycopg2.connect(self.connection_string)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING id",
            (user.username, user.email, user.password),
        )
        user_id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return User(user.username, user.email, user.password, user_id)
