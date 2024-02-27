# tests/interfaces/api/test_user_api.py

import unittest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from interfaces.api.user.user_router import router as user_router
from interfaces.controllers.user_controller import (
    UserController,
)  # Import UserController


class TestUserAPI(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.client = TestClient(user_router)

    def test_register_user(self):
        # Create a mock UserController
        mock_controller = MagicMock()
        mock_controller.register_user.return_value = (
            "User test_user registered successfully"
        )

        # Set the mock controller as the dependency in the router
        user_router.dependency_overrides[UserController] = lambda: mock_controller

        # Make a test request
        request_data = {
            "username": "test_user",
            "email": "test@example.com",
            "password": "password",
        }
        response = self.client.post("/register", json=request_data)

        # Assert that the mock UserController's register_user method was called with the correct arguments
        mock_controller.register_user.assert_called_once_with(request_data)

        # Assert that the response status code is 200 and the response content is as expected
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "User test_user registered successfully")


if __name__ == "__main__":
    unittest.main()
