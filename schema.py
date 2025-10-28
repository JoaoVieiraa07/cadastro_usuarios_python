from pydantic import BaseModel, EmailStr #classe base para validação automática.
from typing import Optional

class UserCreate (BaseModel,EmailStr) : 
    name: str
    email: EmailStr
    telephone: int
class UserResponse (BaseModel,EmailStr) : 
    id: int
    name: str
    email: EmailStr
    telephone: int
    class Config:
        orm_mode = True # permite a criação do modelo de instancia a partir de atributos de outra classe.
class UserUpdate(BaseModel, EmailStr):
    name: Optional[str]
    email: Optional[EmailStr]
    telephone: Optional[int]