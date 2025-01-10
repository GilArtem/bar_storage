# Базовый класс моделей
#from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import as_declarative, declared_attr

@as_declarative()
class Base:
    id: int
    __name__: str
    
    # Генерация имени таблицы по названию класса
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()