from fastapi import FastAPI
from interfaces.api.root_router import router as root_router

app = FastAPI()

app.include_router(root_router)
