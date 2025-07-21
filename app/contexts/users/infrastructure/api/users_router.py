from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import get_user_repository
from app.contexts.users.app.use_cases.get_user_use_case import GetUserUseCase
from app.contexts.users.app.queries.get_user_query import GetUserQuery

router = APIRouter()

class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str

@router.post("/")
def create_user(request: CreateUserRequest):
    # Enviar comando a RabbitMQ (adaptador productor)
    # Aquí deberías implementar la lógica para enviar el comando de creación de usuario
    return {"message": "Comando de creación de usuario enviado"}

@router.get("/{user_id}")
def get_user(user_id: int, user_repository=Depends(get_user_repository)):
    use_case = GetUserUseCase(user_repository)
    user = use_case.execute(GetUserQuery(user_id=user_id))
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user
