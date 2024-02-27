from fastapi import FastAPI
from interfaces.api.root_router import router as root_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(root_router)
