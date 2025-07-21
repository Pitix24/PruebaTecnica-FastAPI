from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str

@router.post("/")
def create_user(request: CreateUserRequest):
    # Enviar comando a RabbitMQ (adaptador productor)
    # ...
    return {"message": "Comando de creación de usuario enviado"}

@router.get("/{user_id}")
def get_user(user_id: int):
    # Ejecutar query directamente (adaptador repositorio)
    # ...
    return {"id": user_id, "name": "Ejemplo", "email": "ejemplo@correo.com"}
