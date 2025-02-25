from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()

@router.post("/auth", tags=["Auth"])
async def add_data(password: str):
    if password != "KLPpassword":
        return JSONResponse(content={"success": False})

    return JSONResponse(content={"success": True})