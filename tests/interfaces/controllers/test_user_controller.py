# tests/interfaces/controllers/test_user_controller.py

import unittest
from unittest.mock import MagicMock
from interfaces.controllers.user_controller import UserController


class TestUserController(unittest.TestCase):
    def test_register_user(self):
        # Create a mock UserRegistration instance
        mock_user_registration = MagicMock()

        # Instantiate UserController with the mock UserRegistration
        user_controller = UserController(mock_user_registration)

        # Call register_user method
        request = {
            "json": {
                "username": "test_user",
                "email": "test@example.com",
                "password": "password",
            }
        }
        response = user_controller.register_user(request)

        # Assert that the mock UserRegistration's register_user method was called with the correct arguments
        mock_user_registration.register_user.assert_called_once_with(
            "test_user", "test@example.com", "password"
        )

        # Assert that the response is as expected
        self.assertEqual(response, "User test_user registered successfully")


if __name__ == "__main__":
    unittest.main()
