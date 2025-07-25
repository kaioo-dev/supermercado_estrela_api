
from datetime import date, time
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

class SaleSchema(BaseModel):
    codigo_venda: int
    cliente_venda: Optional[int] = None
    data_venda: Optional[date] = None
    hora_venda: Optional[time] = None
    desconto_venda: Optional[Decimal] = Decimal("0.00")
    acrescimo_venda: Optional[Decimal] = Decimal("0.00")
    total_venda: Optional[Decimal] = None
    entrada_venda: Optional[Decimal] = Decimal("0.00")
    vendedor_venda: Optional[int] = None
    usuario_venda: Optional[str] = None

    class Config:
        orm_mode = True
