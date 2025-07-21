from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.contexts.users.infrastructure.db.sqlalchemy_user_repository import SQLAlchemyUserRepository
from app.contexts.auth.infrastructure.db.sqlalchemy_auth_repository import SQLAlchemyAuthRepository

DATABASE_URL = "sqlite:///./test.db"  # O usa tu variable de entorno

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_repository(db: Session = None):
    if db is None:
        db = next(get_db())
    return SQLAlchemyUserRepository(db)

def get_auth_repository(db: Session = None):
    if db is None:
        db = next(get_db())
    return SQLAlchemyAuthRepository(db)
