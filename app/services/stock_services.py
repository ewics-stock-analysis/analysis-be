# file for stocks business logic 
import requests
import os
from fastapi import HTTPException

ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_KEY")
alpha_vantage_url = 'https://www.alphavantage.co'

def fetch_intraday_stock_data(ticker: str, interval: str = '5min'):
    """Get intraday stock data """
    if not ALPHA_VANTAGE_API_KEY:
        raise HTTPException(status_code=500, detail='Missing Alpha Vantage API Key')

    url = f"{alpha_vantage_url}/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}&apikey={ALPHA_VANTAGE_API_KEY}"
    
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"Error fetching stock data \n {response.json}")

    data = response.json()
    
    time_series_key = f"Time Series ({interval})"
    
    if time_series_key not in data:
        raise HTTPException(status_code=400, detail=f"Invalid response from Alpha Vantage {data}")

    return data