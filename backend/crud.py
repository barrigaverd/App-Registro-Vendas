from sqlalchemy import func
from sqlalchemy.orm import Session
import models
import schemas
from datetime import date

def create_venda(db: Session, venda: schemas.VendaCreate):
    db_venda = models.Venda(**venda.model_dump())
    db.add(db_venda)
    db.commit()
    db.refresh(db_venda)
    return db_venda

def get_vendas(db: Session, data_filtro: date = None, skip: int = 0, limit: int = 1000):
    query = db.query(models.Venda)
    if data_filtro:
        query = query.filter(func.date(models.Venda.data) == data_filtro)
    return query.order_by(models.Venda.data.desc()).offset(skip).limit(limit).all()

def delete_venda(db: Session, venda_id: int):
    db_venda = db.query(models.Venda).filter(models.Venda.id == venda_id).first()
    if db_venda:
        db.delete(db_venda)
        db.commit()
        return True
    return False

def update_venda(db: Session, venda_id: int, venda_update: schemas.VendaCreate):
    db_venda = db.query(models.Venda).filter(models.Venda.id == venda_id).first()
    if db_venda:
        db_venda.nome = venda_update.nome
        db_venda.valor = venda_update.valor
        db_venda.quantidade = venda_update.quantidade
        db_venda.observacoes = venda_update.observacoes
<<<<<<< HEAD
        db_venda.venda_lancada = venda_update.venda_lancada
=======
        db_venda.lancado = venda_update.lancado
>>>>>>> 0ffe04b (feat: complete frontend admin and backend lancado feature)
        # Preserva a data original se não vier no payload de edição
        if venda_update.data is not None:
            db_venda.data = venda_update.data
        db.commit()
        db.refresh(db_venda)
        return db_venda
    return None