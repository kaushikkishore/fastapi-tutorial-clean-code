from fastapi import APIRouter, HTTPException
from app.usecases.user_registration import UserRegistration
from app.interfaces.repositories import UserRepository
from infrastructure.database.postgres_repository import PostgresUserRepository
from interfaces.controllers.user_controller import UserController

router = APIRouter()

# Dependency injection
user_repository = PostgresUserRepository(connection_string="your_db_connection_string")
user_registration = UserRegistration(user_repository)
user_controller = UserController(user_registration)


@router.post("/register")
async def register_user(username: str, email: str, password: str):
    request = {"json": {"username": username, "email": email, "password": password}}
    return user_controller.register_user(request)
