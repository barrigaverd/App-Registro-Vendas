from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal
from datetime import date
router = APIRouter(prefix="/vendas", tags=["Vendas"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Venda)
def create_venda(venda: schemas.VendaCreate, db: Session = Depends(get_db)):
    return crud.create_venda(db=db, venda=venda)

@router.get("/", response_model=list[schemas.Venda])
def list_vendas(data: date = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_vendas(db=db, data_filtro=data, skip=skip, limit=limit)

@router.delete("/{venda_id}")
def delete_venda(venda_id: int, db: Session = Depends(get_db)):
    sucesso = crud.delete_venda(db=db, venda_id=venda_id)
    if sucesso:
        return {"ok": True}
    else:
        raise HTTPException(status_code=404, detail="Venda não encontrada")

@router.put("/{venda_id}", response_model=schemas.Venda)
def update_venda(venda_id: int, venda_update: schemas.VendaCreate, db: Session = Depends(get_db)):
    db_venda = crud.update_venda(db=db, venda_id=venda_id, venda_update=venda_update)    
    if db_venda is None:
        raise HTTPException(status_code=404, detail="Venda não encontrada")
    else:
        return db_venda
