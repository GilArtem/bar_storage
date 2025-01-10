# Реализация схемы для создания пользователя
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    
class UserCreate(UserBase):
    email: str
    password: str
    is_active: bool = True  # значение по умолчанию
    is_superuser: bool = False  # значение по умолчанию
    
class UserOut(UserBase):
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True
        