from dotenv import load_dotenv
from fastapi import Depends, FastAPI

from .middleware.auth_middleware import APIKeyMiddleware
from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import stocks
from .config import config 

#app = FastAPI(dependencies=[Depends(get_query_token)])
load_dotenv()

app = FastAPI()
print(f"Running in {config.environment} mode")

app.add_middleware(APIKeyMiddleware)

app.include_router(stocks.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    #dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}