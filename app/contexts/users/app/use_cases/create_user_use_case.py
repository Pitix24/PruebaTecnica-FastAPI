from ...domain.repo.user_repo import UserRepository
from ...domain.entities.user import User
from ..commands.create_user_command import CreateUserCommand
import hashlib

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, command: CreateUserCommand) -> User:
        password_hash = hashlib.sha256(command.password.encode()).hexdigest()
        user = User(id=None, name=command.name, email=command.email, password_hash=password_hash)
        return self.user_repository.add(user)
