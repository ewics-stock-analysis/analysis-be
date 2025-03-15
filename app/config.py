import os
from dotenv import load_dotenv

class Config:
    
    def __init__(self):
        load_dotenv()

        self.environment = os.getenv("ENV", "DEV")

        # Use demo key for dev because only 25 requests/day 
        self.alpha_vantage_key = (
            "demo" if self.environment == "DEV" else os.getenv("ALPHA_VANTAGE_API_KEY")
        )

        # Base URL for Alpha Vantage
        self.alpha_vantage_url = "https://www.alphavantage.co"

    def is_dev(self):
        return self.environment == "DEV"

    def is_prod(self):
        return self.environment == "PROD"

config = Config()
