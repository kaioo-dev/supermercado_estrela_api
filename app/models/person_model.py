from sqlalchemy import Column, Integer, String
from .base import Base


class PersonModel(Base):
    __tablename__ = "pessoas"

    codigo_pessoa = Column("codi_pes", Integer, primary_key=True, index=True)
    nome_pessoa = Column("nome_pes", String(60), nullable=False)
