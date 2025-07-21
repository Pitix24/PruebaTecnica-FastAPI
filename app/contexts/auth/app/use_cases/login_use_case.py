from ...domain.repo.auth_repo import AuthRepository
from ...domain.entities.auth_token import AuthToken
from datetime import datetime, timedelta
import jwt  # PyJWT
import hashlib

class LoginUseCase:
    def __init__(self, auth_repository: AuthRepository, user_repository, secret_key: str):
        self.auth_repository = auth_repository
        self.user_repository = user_repository
        self.secret_key = secret_key

    def execute(self, command):
        # Buscar usuario por email
        user = self.user_repository.get_by_email(command.email)
        if not user:
            raise Exception("Invalid credentials")
        # Verificar contraseña (hash)
        password_hash = hashlib.sha256(command.password.encode()).hexdigest()
        if user.password_hash != password_hash:
            raise Exception("Invalid credentials")
        # Generar tokens
        access_token = jwt.encode(
            {"sub": user.id, "exp": datetime.utcnow() + timedelta(minutes=30)},
            self.secret_key,
            algorithm="HS256"
        )
        refresh_token = jwt.encode(
            {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=7)},
            self.secret_key,
            algorithm="HS256"
        )
        token = AuthToken(
            access_token=access_token,
            refresh_token=refresh_token,
            user_id=user.id,
            expires_at=datetime.utcnow() + timedelta(minutes=30)
        )
        self.auth_repository.save_token(token)
        return token
