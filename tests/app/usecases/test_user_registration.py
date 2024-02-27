# tests/app/usecases/test_user_registration.py

import unittest
from unittest.mock import MagicMock
from app.usecases.user_registration import UserRegistration
from app.entities.user import User


class TestUserRegistration(unittest.TestCase):
    def test_register_user(self):
        # Create a mock UserRepository
        mock_repository = MagicMock()
        mock_repository.save.return_value = User(
            "test_user", "test@example.com", "password", 1
        )

        # Instantiate UserRegistration with the mock repository
        user_registration = UserRegistration(mock_repository)

        # Call register_user method
        user = user_registration.register_user(
            "test_user", "test@example.com", "password"
        )

        # Assert that the repository's save method was called with the correct arguments
        mock_repository.save.assert_called_once_with(
            User("test_user", "test@example.com", "password")
        )

        # Assert that the returned user object is as expected
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.id, 1)


if __name__ == "__main__":
    unittest.main()
