# tests/app/entities/test_user.py

import unittest
from app.entities.user import User


class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("test_user", "test@example.com", "password")

        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")


if __name__ == "__main__":
    unittest.main()
