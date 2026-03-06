from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from database import Base
from datetime import datetime
class Venda(Base):
    __tablename__ = "vendas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    valor = Column(Float)
    quantidade = Column(Integer, default=1)
    observacoes = Column(String, nullable=True)
    data = Column(DateTime, default=datetime.utcnow)
    venda_lancada = Column(Boolean, default=False)