# Здесь будет храниться информация о подключении к базе данных:
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"







# from pydantic import BaseSettings

# class Settings(BaseSettings):
#     DATABASE_URL: str = "postgresql+psycopg2://postgres:letsgo@db:5432/bar_inventory"
    
#     class Config:
#         env_file = ".env"