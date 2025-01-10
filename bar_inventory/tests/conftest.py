# Фикстура db_session
# Наше приложение выполняет только базовые операции CRUD, 
# поэтому можно использовать SQLite для большей скорости в юнит-тестах, 
# (но интеграционные тесты должны быть на PostgreSQL).
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base

# SQLite фикстура
@pytest.fixture(scope="function")
def sqlite_session():
    """Создает сессию для тестов с SQLite"""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)  # Пересоздаем таблицы
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)  # Удаляем таблицы

# PostgreSQL фикстура
DATABASE_URL = "postgresql+psycopg2://test_user:test_password@localhost:5433/test_db"

@pytest.fixture(scope="function")
def postgres_session():
    """Создает сессию для тестов с PostgreSQL"""
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
