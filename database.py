from sqlalchemy import create_engine #importando para a criação do banco
from sqlalchemy.ext.declarative import declarative_base #função base para que eu possa a chamar depois
from sqlalchemy.orm import sessionmaker #criação da sessão para interagir com o banco
DATABASE_URL = "sqlite:///./cadastrar_usuarios.db" #url do banco de dados
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) #para checar se não possui nenhuma thread igual, garantindo alguns erros a menos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #autocommit = para que não se atualize o banco sem commitar. autoflush = permite fazer operações de inserção, atualização e exclusão diretamente em objetos em python
Base = declarative_base() #função base
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()