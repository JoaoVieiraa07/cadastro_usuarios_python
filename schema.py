from pydantic import BaseModel #classe base para validação automática.
class UserCreate (BaseModel) : 
    name: str
    email: str
    telephone: int
class UserResponse (BaseModel) : 
    id: int
    name: str
    email: str
    telephone: int
    class Config:
        orm_mode = True # permite a criação do modelo de instancia a partir de atributos de outra classe.