from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import get_auth_repository, get_user_repository
from app.contexts.auth.app.use_cases.login_use_case import LoginUseCase
from app.contexts.auth.app.commands.login_command import LoginCommand

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class LogoutRequest(BaseModel):
    access_token: str

@router.post("/login")
def login(request: LoginCommand, 
          auth_repository=Depends(get_auth_repository), 
          user_repository=Depends(get_user_repository)):
    use_case = LoginUseCase(auth_repository, user_repository, secret_key="supersecret")
    try:
        token = use_case.execute(request)
        return {"access_token": token.access_token, "refresh_token": token.refresh_token}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

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
