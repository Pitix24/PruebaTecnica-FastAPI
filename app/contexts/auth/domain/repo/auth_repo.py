from abc import ABC, abstractmethod
from .entities.auth_token import AuthToken

class AuthRepository(ABC):
    @abstractmethod
    def save_token(self, token: AuthToken) -> None:
        pass

    @abstractmethod
    def get_token(self, access_token: str) -> AuthToken:
        pass

    @abstractmethod
    def revoke_token(self, access_token: str) -> None:
        pass