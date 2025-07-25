from typing import List
from sqlalchemy.orm import Session
from datetime import date

from drivers import SessionLocal
from models import PersonModel, SaleModel
from schemas import SaleSchema

class SaleRepository:

    def get_sales_per_day(self, start_date: date, end_date: date) -> List[SaleSchema]:
        session_db: Session = SessionLocal()
        try:
            result = (
                session_db.query(SaleModel)
                .filter(SaleModel.data_venda >= start_date)
                .filter(SaleModel.data_venda <= end_date)
                .order_by(SaleModel.data_venda.asc())
                .all()
            )
            return_list: List[SaleSchema] = []
            for sale in result:
                return_list.append(
                    SaleSchema(
                        codigo_venda=sale.codigo_venda,
                        cliente_venda=sale.cliente_venda,
                        data_venda=sale.data_venda,
                        hora_venda=sale.hora_venda,
                        desconto_venda=sale.desconto_venda,
                        acrescimo_venda=sale.acrescimo_venda,
                        total_venda=sale.total_venda,
                        entrada_venda=sale.entrada_venda,
                        vendedor_venda=sale.vendedor_venda,
                        usuario_venda=sale.usuario_venda
                    )
                )
            return return_list
        finally:
            session_db.close()

    def _get_code_and_name_person_by_code(self, codigo_cliente: int) -> str:
        session_db: Session = SessionLocal()
        try:
            person = (
                session_db.query(PersonModel.codigo_pessoa, PersonModel.nome_pessoa)
                .filter(PersonModel.codigo_pessoa == codigo_cliente)
                .first()
            )
            if person:
                return f"{person.codigo_pessoa} - {person.nome_pessoa}"
            else:
                return "Cliente não encontrado"
        finally:
            session_db.close()
