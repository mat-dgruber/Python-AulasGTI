from fastapi import APIRouter, status, Response
from .endpoints.users import router as UserRouter


# Declarando o Router
api_router = APIRouter()

# Definindo o Router Filho
api_router.include_router(UserRouter, prefix="/users") 