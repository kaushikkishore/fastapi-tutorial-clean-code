# tests/infrastructure/database/test_postgres_repository.py

import unittest
from unittest.mock import MagicMock
from infrastructure.database.postgres_repository import PostgresUserRepository
from app.entities.user import User


class TestPostgresUserRepository(unittest.TestCase):
    def test_save_user(self):
        # Create a mock connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        # Instantiate PostgresUserRepository with the mock connection
        postgres_repo = PostgresUserRepository(
            connection_string="test_connection_string"
        )
        postgres_repo._get_connection = MagicMock(return_value=mock_conn)

        # Call save method
        user = User("test_user", "test@example.com", "password")
        saved_user = postgres_repo.save(user)

        # Assert that the cursor's execute method was called with the correct SQL query
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING id",
            ("test_user", "test@example.com", "password"),
        )

        # Assert that the returned user object is as expected
        self.assertEqual(saved_user.username, "test_user")
        self.assertEqual(saved_user.email, "test@example.com")
        self.assertEqual(saved_user.password, "password")


if __name__ == "__main__":
    unittest.main()
