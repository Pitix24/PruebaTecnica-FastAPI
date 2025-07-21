from ...domain.repo.user_repo import UserRepository
from ...domain.entities.user import User
from sqlalchemy.orm import Session
from app.core.db_models import UserModel

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add(self, user: User) -> User:
        user_model = UserModel(name=user.name, email=user.email, password_hash=user.password_hash)
        self.db_session.add(user_model)
        self.db_session.commit()
        return User(id=user_model.id, name=user_model.name, email=user_model.email, password_hash=user_model.password_hash)

    def get_by_id(self, user_id: int) -> User:
        user_model = self.db_session.query(UserModel).filter_by(id=user_id).first()
        if user_model:
            return User(id=user_model.id, name=user_model.name, email=user_model.email, password_hash=user_model.password_hash)
        return None
