<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
=======
# 1. Importe Column, Integer, String, Float, DateTime da biblioteca sqlalchemy
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
# 2. Importe o 'Base' que você criou no arquivo database.py
>>>>>>> 0ffe04b (feat: complete frontend admin and backend lancado feature)
from database import Base
from datetime import datetime
class Venda(Base):
    __tablename__ = "vendas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    valor = Column(Float)
    quantidade = Column(Integer, default=1)
    observacoes = Column(String, nullable=True)
<<<<<<< HEAD
    data = Column(DateTime, default=datetime.utcnow)
    venda_lancada = Column(Boolean, default=False)
=======
    # 4.7. Crie o campo 'data': tipo DateTime, com o valor padrão sendo o horário atual (datetime.utcnow)
    data = Column(DateTime, default=datetime.utcnow)
    # 4.8. Crie o campo 'lancado': tipo Boolean, com valor padrão Falso
    lancado = Column(Boolean, default=False)
>>>>>>> 0ffe04b (feat: complete frontend admin and backend lancado feature)
