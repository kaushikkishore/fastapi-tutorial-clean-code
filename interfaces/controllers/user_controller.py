from app.usecases.user_registration import UserRegistration
import json


class UserController:
    def __init__(self, user_registration: UserRegistration):
        self.user_registration = user_registration

    def register_user(self, request):
        username = request["json"]["username"]
        email = request["json"]["email"]
        password = request["json"]["password"]
        user = self.user_registration.register_user(username, email, password)
        return f"User {user.username} registered successfully"
