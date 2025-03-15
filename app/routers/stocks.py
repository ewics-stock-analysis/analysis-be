from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header
from ..services import stock_services

router = APIRouter()

router = APIRouter(
    prefix="/stocks",
    tags=["stocks"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["stocks"])
async def read_stocks():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/{ticker}", tags=["stocks"])
async def read_stocks(ticker: str):
    return stock_services.fetch_intraday_stock_data(ticker)
