from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schema as schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/", response_model=schemas.UserResponse)
def criar_usuario(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.pegar_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return crud.criar_usuario(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def ver_usuario(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.pegar_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user

@app.delete("/users/{user_id}")
def excluir_usuario(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.pegar_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    crud.excluir_usuario(db=db, user_id=user_id)
    return {"message": "Usuário deletado com sucesso"}