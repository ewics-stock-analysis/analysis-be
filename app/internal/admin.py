# For admin routes, might not need this but I'll throw it in here anyways
from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}