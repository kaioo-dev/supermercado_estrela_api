from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import fdb

# Carregar DLL Firebird correta
fdb.load_api("C:/Users/kaioa/Desktop/ESTUDOS/supermercado_estrela_api/fbclient.dll")

DATABASE_URL = "firebird+fdb://sysdba:masterkey@26.2.70.125:3050/c:/Controle/banco/BANCO.FDB?charset=UTF8"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


if __name__ == "__main__":
    session = SessionLocal()
    try:
        result = session.execute(text("SELECT * FROM pessoas")).fetchall()
        for row in result:
            print(row)
        print("Conexão e consulta bem-sucedidas!")
    except Exception as e:
        print("Erro na conexão ou consulta:", e)
    finally:
        session.close()