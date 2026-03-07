from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class VendaBase(BaseModel):
    nome: str
    valor: float
    quantidade: int = 1
    observacoes: Optional[str] = None
    data: Optional[datetime] = None
<<<<<<< HEAD
    venda_lancada: Optional[bool] = False
=======
    lancado: bool = False
>>>>>>> 0ffe04b (feat: complete frontend admin and backend lancado feature)

class VendaCreate(VendaBase):
    pass

class Venda(VendaBase):
    id: int 
    model_config = ConfigDict(from_attributes=True)