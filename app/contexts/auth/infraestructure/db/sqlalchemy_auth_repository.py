from ...domain.repo.auth_repo import AuthRepository
from ...domain.entities.auth_token import AuthToken
from sqlalchemy.orm import Session
from app.core.db_models import AuthTokenModel

class SQLAlchemyAuthRepository(AuthRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def save_token(self, token: AuthToken) -> None:
        token_model = AuthTokenModel(
            access_token=token.access_token,
            refresh_token=token.refresh_token,
            user_id=token.user_id,
            expires_at=token.expires_at
        )
        self.db_session.add(token_model)
        self.db_session.commit()

    def get_token(self, access_token: str) -> AuthToken:
        token_model = self.db_session.query(AuthTokenModel).filter_by(access_token=access_token).first()
        if token_model:
            return AuthToken(
                access_token=token_model.access_token,
                refresh_token=token_model.refresh_token,
                user_id=token_model.user_id,
                expires_at=token_model.expires_at
            )
        return None

    def revoke_token(self, access_token: str) -> None:
        token_model = self.db_session.query(AuthTokenModel).filter_by(access_token=access_token).first()
        if token_model:
            self.db_session.delete(token_model)
            self.db_session.commit()
