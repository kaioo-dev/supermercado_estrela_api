from typing import List

from sqlalchemy.orm import Session

from datetime import date
from drivers import SessionLocal
from models import PersonModel, SaleModel
from schemas import PersonSchema, SaleSchema



class SaleRepository:

    def get_sales_per_day(self, start_date: date, end_date: date) -> List[SaleSchema]:
        session_db: Session = SessionLocal

        try:
            return_list: List[SaleSchema] = []
            result = (
                session_db.query(SaleModel)
                .filter(SaleModel.data_venda >= start_date)
                .filter(SaleModel.data_venda <= end_date)
                .order_by(SaleModel.data_venda.asc())
                .all()
            )
            for sale in result:
                return_list.append(
                    SaleSchema(
                        codigo_venda=sale.codigo_venda,
                        cliente_venda=self._get_code_and_name_person_by_code(sale.cliente_venda),
                        data_venda=sale.data_venda,
                        hora_venda=sale.hora_venda,
                        desconto_venda=sale.desconto_venda,
                        acrescimo_venda=sale.acrescimo_venda,
                        total_venda=sale.total_venda,
                        entrada_venda=sale.entrada_venda,
                        vendedor_venda=self._get_code_and_name_person_by_code(sale.vendedor_venda),
                        usuario_venda=sale.usuario_venda
                    )
                )
            return result
        finally:
            session_db.close()

    def _get_code_and_name_person_by_code(self, codigo_cliente: int) -> str:
        session_db: Session = SessionLocal

        try:
            person: PersonModel = (
                session_db.query(
                    PersonModel.codigo_pessoa, 
                    PersonModel.nome_pessoa
                ).filter(
                    PersonModel.codigo_pessoa == codigo_cliente
                ).first()
            )
            return person.codigo_pessoa + ' - ' + person.nome_pessoa
        finally:
            session_db.close()