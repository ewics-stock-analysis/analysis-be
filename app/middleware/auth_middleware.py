# Middleware to ensure API key is set before processing requests.
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import os

class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        api_key = os.getenv("ALPHA_VANTAGE_KEY")

        if not api_key:
            raise HTTPException(status_code=500, detail="Missing Alpha Vantage API Key. Please configure your environment.")

        response = await call_next(request)  # Continue processing request
        return response
