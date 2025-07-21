from ...domain.repo.auth_repo import AuthRepository

class LogoutUseCase:
    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository

    def execute(self, command):
        self.auth_repository.revoke_token(command.access_token)
