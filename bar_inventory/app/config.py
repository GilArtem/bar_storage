# Здесь будет храниться информация о подключении к базе данных:
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

