from ...domain.repo.auth_repo import AuthRepository

class ValidateTokenUseCase:
    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository

    def execute(self, query):
        token = self.auth_repository.get_token(query.access_token)
        if not token:
            raise Exception("Token inválido o expirado")
        return token
