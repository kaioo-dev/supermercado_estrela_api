from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base  


DB_USER = "SYSDBA"
DB_PASSWORD = "MASTERKEY"
DB_HOST = "26.2.70.125:3050"
DB_PATH = "C:\Controle\banco\BANCO.FDB"
DB_CHARSET = "UTF8"

DATABASE_URL = f"firebird+fdb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_PATH}?charset={DB_CHARSET}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # (Opcional) Criar tabelas automaticamente se ainda não existirem
# def init_db():
#     Base.metadata.create_all(bind=engine)
