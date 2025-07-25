from sqlalchemy import (
    Column, Integer, Date, Time, Numeric, String, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base import Base


class SaleModel(Base):
    __tablename__ = "vendas"

    codigo_venda = Column("codi_ven", Integer, primary_key=True, index=True)
    cliente_venda = Column("clie_ven", Integer, ForeignKey("pessoas.codi_pes"), nullable=False)
    data_venda = Column("data_ven", Date, nullable=False)
    hora_venda = Column("hora_ven", Time, nullable=False)
    desconto_venda = Column("desc_ven", Numeric(10, 2), nullable=True)
    acrescimo_venda = Column("acre_ven", Numeric(10, 2), nullable=True)
    total_venda = Column("tota_ven", Numeric(10, 2), nullable=False)
    entrada_venda = Column("entr_ven", Numeric(10, 2), nullable=True)
    vendedor_venda = Column("vend_ven", Integer, ForeignKey("pessoas.codi_pes"), nullable=False)
    usuario_venda = Column("usua_ven", String(20), nullable=False)

    # Relacionamentos opcionais
    cliente = relationship("PersonModel", foreign_keys=[cliente_venda], backref="compras")
    vendedor = relationship("PersonModel", foreign_keys=[vendedor_venda], backref="vendas_realizadas")
