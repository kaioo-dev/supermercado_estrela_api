from datetime import date

from fastapi import HTTPException

from repositories import SaleRepository


class SaleUseCase:
    def __init__(self):
        self.sale_repository: SaleRepository = SaleRepository()

    def get_sales_per_day(self, start_date: date, end_date: date):
        try:
            return self.sale_repository.get_sales_per_day(start_date, end_date)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))