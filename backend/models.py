# 1. Importe Column, Integer, String, Float, DateTime da biblioteca sqlalchemy
from sqlalchemy import Column, Integer, String, Float, DateTime
# 2. Importe o 'Base' que você criou no arquivo database.py
from database import Base
# 3. Importe o 'datetime' do módulo datetime para usar como valor padrão
from datetime import datetime
# 4. Crie uma classe chamada 'Venda' que herda de 'Base'
class Venda(Base):
    # 4.1. Defina o nome da tabela no banco de dados como "vendas"
    __tablename__ = "vendas"
    # 4.2. Crie o campo 'id': tipo Inteiro, Chave Primária, com indexação
    id = Column(Integer, primary_key=True, index=True)
    # 4.3. Crie o campo 'nome': tipo String
    nome = Column(String)
    # 4.4. Crie o campo 'valor': tipo Float
    valor = Column(Float)
    # 4.5. Crie o campo 'quantidade': tipo Inteiro, com valor padrão (default) de 1
    quantidade = Column(Integer, default=1)
    # 4.6. Crie o campo 'observacoes': tipo String, permitindo que seja nulo (nullable=True)
    observacoes = Column(String, nullable=True)
    # 4.7. Crie o campo 'data': tipo DateTime, com o valor padrão sendo o horário atual (datetime.utcnow)
    data = Column(DateTime, default=datetime.utcnow)