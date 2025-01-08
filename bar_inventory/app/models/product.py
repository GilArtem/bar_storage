# Пример модели "Product"
from sqlalchemy import Column, Integer, String, Float
from app.models.base import Base

class Product(Base):
    __tablename__="product"
    
    id = Column(Integer, primary_key=True, index=True) # index нужен для более быстрого доступа
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=False)
    
    