from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class LogoutRequest(BaseModel):
    access_token: str

@router.post("/login")
def login(request: LoginRequest):
    # Enviar comando a RabbitMQ (adaptador productor)
    # ...
    return {"message": "Comando de login enviado"}

@router.post("/logout")
def logout(request: LogoutRequest):
    # Enviar comando a RabbitMQ (adaptador productor)
    # ...
    return {"message": "Comando de logout enviado"}

@router.get("/validate")
def validate_token(access_token: str):
    # Ejecutar query directamente (adaptador repositorio)
    # ...
    return {"valid": True, "user_id": 1}
