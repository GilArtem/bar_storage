# Здесь будет настройка подключения к базе данных:

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config import Settings

settings = Settings()

engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Dependency для получения сессии
async def get_session() -> AsyncSession: # type: ignore
    async with async_session() as session:
        yield session