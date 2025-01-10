from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.security import hash_password
from typing import Optional


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """Получение пользователя по email"""
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    """Получение пользователя по ID"""
    return db.query(User).filter(User.id == user_id).first()


def create_user(db_session, user_data: UserCreate):
    hashed_password = hash_password(user_data.password)  # хэшируем пароль
    user = User(
        email=user_data.email,
        hashed_password=hashed_password,
        is_active=user_data.is_active,  # устанавливаем значение
        is_superuser=user_data.is_superuser  # устанавливаем значение
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user