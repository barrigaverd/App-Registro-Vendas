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

def get_vendas(db: Session, data_filtro: date = None, skip: int = 0, limit: int = 100):
    query = db.query(models.Venda)
    # Se nenhum filtro passado, usa hoje por padrão
    filtro = data_filtro if data_filtro else date.today()
    query = query.filter(func.date(models.Venda.data) == filtro)
    return query.offset(skip).limit(limit).all()

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
        db_venda.venda_lancada = venda_update.venda_lancada
        # Preserva a data original se não vier no payload de edição
        if venda_update.data is not None:
            db_venda.data = venda_update.data
        db.commit()
        db.refresh(db_venda)
        return db_venda
    return None