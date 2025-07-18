import base64
from datetime import date

from fastapi import APIRouter, Depends, UploadFile

from use_cases import SaleUseCase


router = APIRouter()


def get_sale_use_case() -> SaleUseCase:
    return SaleUseCase()


def file_to_base64(file: UploadFile) -> bytes:
    if not file:
        return b""
    return base64.b64encode(file.file.read())


@router.get(
    "/sale",
    tags=["Sale"],
)
def get_sales_per_day(
    analysis_use_case: SaleUseCase = Depends(get_sale_use_case),
    start_date: date = ...,
    end_date: date = ...
):
    return analysis_use_case.get_sales_per_day(start_date, end_date)