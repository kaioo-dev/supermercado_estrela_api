from pydantic import BaseModel
from datetime import date, time
from typing import Optional
from decimal import Decimal

class SaleSchema(BaseModel):
    codigo_venda: int
    cliente_venda: str
    data_venda: date
    hora_venda: time
    desconto_venda: Optional[Decimal] = Decimal("0.00")
    acrescimo_venda: Optional[Decimal] = Decimal("0.00")
    total_venda: Decimal
    entrada_venda: Optional[Decimal] = Decimal("0.00")
    vendedor_venda: str
    usuario_venda: str

    class Config:
        orm_mode = True
