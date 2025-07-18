from datetime import date


class SaleRepository:
    def __init__(self):
        self.db = ...

    def get_sales_per_day(self, start_date: date, end_date: date):
        return {"start_date": start_date, "end_date": end_date}
