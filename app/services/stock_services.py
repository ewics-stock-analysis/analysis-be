# file for stocks business logic 
import requests
from fastapi import HTTPException
from ..config import config 


def fetch_intraday_stock_data(ticker: str, interval: str = '5min'):
    """Get intraday stock data """
    url = f"{config.alpha_vantage_url}/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}&apikey={config.alpha_vantage_key}"
    
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"Error fetching stock data \n {response.json}")

    data = response.json()
    
    time_series_key = f"Time Series ({interval})"
    
    if time_series_key not in data:
        raise HTTPException(status_code=400, detail=f"Invalid response from Alpha Vantage {data}")

    return data

# returns the top 20 gainers, losers in past day
def fetch_top_losers_gainers():
    url = f"{config.alpha_vantage_url}/query?function=TOP_GAINERS_LOSERS&apikey={config.alpha_vantage_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"Error fetching stock data \n {response.json()}")
    data = response.json()
    if 'top_gainers' not in data:
        raise HTTPException(status_code=400, detail=f"Invalid response from Alpha Vantage {data}")
    return data