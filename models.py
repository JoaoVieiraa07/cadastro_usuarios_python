from sqlalchemy import Column, Integer, String  #Serve para importar a coluna, números inteiros, e as strings.
from .database import Base #Função base que já havia sido criada no database
class User(Base): #aqui eu chamo aquela função base para a tabela user
    __tablename__ = "users" #nome da tabela

    id = Column(Integer, primary_key=True) #id da conta/contato, e por aí vai
    name = Column(String, index=True) 
    email = Column(String, unique=True, index=True)
    telephone = Column(Integer, unique=True, index=True)