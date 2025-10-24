from sqlalchemy.orm import Session #Importando a sessão para que o banco faça a ligação. Além disso também utilizando orm (instancia)
from .models import User #Importando a tabela user.
from .schema import UserCreate #Importando a parte da criação do usuário.

def pegar_id(db: Session, user_id : int): #função para pegar o id que ira utilizar a session do banco de dados e o user_id(id do usuário)
    return db.query(User).filter(User.id == user_id).first() #Leitura da linha : ela vai retornar como uma consulta na tabela user, buscando apenas o que for o id do usuario for igual ao id do usuario passado.

def criar_usuario(db: Session, user: UserCreate): #chamando a função do usercreate para a criação do usuário
    db_user = User(name=user.name, email=user.email, telephone =user.telephone) #apenas fazendo 
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

